# robot-fan

The fan model built using LEGO® MINDSTORMS® Robot Inventor.

_**Disclaimer:** LEGO® and MINDSTORMS® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this project._

## Features

- touch control to turn on and off:
  - based on LEGO® MINDSTORMS® Color Sensor;
- proportional control of the rotation speed:
  - based on LEGO® MINDSTORMS® Medium Motor;
- touch and proportional controls are independent.

## Testing

To run the unit tests, use the following command:

```
$ make test
```

## Building

For the convenience of uploading the script to the LEGO® MINDSTORMS® intelligent Hub, it is worth combining all parts of the project together.

To do this, use the following command:

```
$ make build
```

The resulting file will be available at path `builds/robot_fan.py`.

## License

The MIT License (MIT)

Copyright &copy; 2021 thewizardplusplus
