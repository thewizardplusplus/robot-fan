# robot-fan

_**Disclaimer:** LEGO® and MINDSTORMS® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this project._

## Testing

```
$ python3 -m unittest discover -p '*_test.py'
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
