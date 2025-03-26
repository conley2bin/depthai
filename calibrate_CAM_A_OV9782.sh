# calibrate_CAM_A_OV9782.sh Description: Calibrate camera CAM_A_OV9782

# squareSizeCm: 4.42cm
# markerSizeCm: 3.30cm
# squaresX: 13
# squaresY: 7
# cameraMode: perspective
# disableCamera: left, right

python calibrate.py --squareSizeCm 4.42 \
                    --markerSizeCm 3.30 \
                    --squaresX 13 \
                    --squaresY 7 \
                    --cameraMode perspective \
                    --disableCamera left right\
                    --enablePolygonsDisplay \
                    --mode process \