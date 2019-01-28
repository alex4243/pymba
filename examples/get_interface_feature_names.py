from pymba import Vimba


if __name__ == '__main__':

    with Vimba() as vmb:
        interface = vmb.interface(0)
        interface.open()

        for feature_name in interface.feature_names():
            print(feature_name)

        interface.close()
