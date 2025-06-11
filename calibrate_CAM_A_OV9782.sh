# calibrate_CAM_A_OV9782.sh Description: Calibrate camera CAM_A_OV9782

# Hfov140_dataset:
python calibrate.py --squareSizeCm 4.42 \
                    --markerSizeCm 3.30 \
                    --squaresX 13 \
                    --squaresY 7 \
                    --cameraMode perspective \
                    --disableCamera left right \
                    --enablePolygonsDisplay \
                    --board OAK-FFC-4P \
                    --mode process \

# # Hfov180_dataset:
# python calibrate.py --squareSizeCm 3.95 \
#                     --markerSizeCm 2.95 \
#                     --squaresX 13 \
#                     --squaresY 7 \
#                     --cameraMode Fisheye \
#                     --disableCamera left right \
#                     --enablePolygonsDisplay \
#                     --board OAK-FFC-4P \
#                     --mode process \