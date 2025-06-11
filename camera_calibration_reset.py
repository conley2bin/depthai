#!/usr/bin/env python3
# save_as_camera_calibration_reset.py
import argparse
import depthai as dai
import json
import time
import sys
import os

def load_calibration(calibration_file):
   """加载校准文件"""
   try:
       with open(calibration_file, "r") as f:
           calibration_data = json.load(f)
       
       # 打印相机类型信息
       if len(calibration_data["cameraData"]) > 0 and len(calibration_data["cameraData"][0]) > 1:
           current_type = calibration_data["cameraData"][0][1].get("cameraType", None)
           camera_type_str = "透视模式" if current_type == 0 else "鱼眼模式" if current_type == 1 else f"未知模式({current_type})"
           print(f"校准文件相机类型: {camera_type_str}")
       
       return calibration_data
   except Exception as e:
       print(f"读取校准文件失败: {e}")
       sys.exit(1)

def reset_and_flash_calibration(calibration_file):
   """重置并写入校准数据"""
   max_attempts = 3
   
   for attempt in range(max_attempts):
       try:
           print(f"\n尝试 {attempt+1}/{max_attempts}:")
           
           # 连接设备
           print("连接设备...")
           device = dai.Device()
           
           # 尝试重置校准数据
           try:
               print("重置现有校准数据...")
               device.factoryResetCalibration()
               print("✅ 重置成功")
           except Exception as e:
               print(f"⚠️ 重置校准失败: {e}")
               print("继续尝试写入校准数据...")
           
           # 关闭设备连接
           device.close()
           print("设备已断开。等待5秒后重新连接...")
           time.sleep(5)
           
           # 重新连接并写入校准数据
           print("重新连接设备...")
           device = dai.Device()
           print("写入校准数据...")
           
           calib_handler = dai.CalibrationHandler(calibration_file)
           success = device.flashCalibration(calib_handler)
           
           if success:
               print("✅ 校准数据已成功写入设备!")
               device.close()
               return True
           else:
               print("❌ 写入校准数据失败!")
               device.close()
       
       except Exception as e:
           print(f"❌ 操作失败: {e}")
       
       if attempt < max_attempts - 1:
           print(f"\n等待10秒后重试...")
           time.sleep(10)
   
   return False

def main():
   # 解析命令行参数
   parser = argparse.ArgumentParser(description="重置并写入相机校准数据")
   parser.add_argument("calibration_file", help="校准JSON文件路径")
   args = parser.parse_args()
   
   if not os.path.exists(args.calibration_file):
       print(f"错误: 校准文件 '{args.calibration_file}' 不存在")
       sys.exit(1)
   
   print("=" * 50)
   print("相机校准重置工具")
   print("=" * 50)
   
   print("\n1. 加载校准文件...")
   load_calibration(args.calibration_file)
   
   print("\n2. 请确保没有其他程序正在使用相机")
   print("   建议: 断开相机USB连接, 等待5秒, 然后重新连接")
   input("准备好后按回车键继续...")
   
   print("\n3. 重置并写入校准数据...")
   success = reset_and_flash_calibration(args.calibration_file)
   
   print("\n" + "=" * 50)
   if success:
       print("✅ 操作完成！校准数据已成功写入设备")
       print("   如果遇到问题，请尝试重启相机和计算机")
   else:
       print("❌ 操作失败！请尝试以下步骤:")
       print("   1. 重启计算机")
       print("   2. 使用不同的USB端口")
       print("   3. 检查相机是否有物理损坏")
   print("=" * 50)

if __name__ == "__main__":
   main()
