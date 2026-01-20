class DeviceNotOnError(Exception):
    pass

class DeviceNotFoundError(Exception):
    pass

class Device:
    def __init__(self,name):
        self._name = name
        self._status = False

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value):
        self._status = value
        print(f"[{self._name}]的开启状态为：{value}")

class Light(Device):
    def __init__(self,name,brightness = 0):
        super().__init__(name)
        self._brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self,value):
        self.status = True
        self._brightness = value
        print(f"[{self._name}]的亮度设置为：{value}")

class AirConditioner(Device):
    def __init__(self,name,temperature = 0):
        super().__init__(name)
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        self.status = True
        self._temperature = value
        print(f"[{self._name}]的温度设置为：{value}")

class SecurityCamera(Device):
    def __init__(self,name,recording = False):
        super().__init__(name)
        self._recording = recording

    @property
    def recording(self):
        return self._recording

    @recording.setter
    def recording(self,value):
        if self.status:
            self._recording = value
            print(f"[{self._name}]的录制状态为：{value}")
        else:
            raise DeviceNotonError(f"[{self._name}]设备未开启")

class SmartHomeSystem:
    def __init__(self):
        self.data = {}
    
    def add_device(self,name):
        self.data[name._name] = name
        print(f"设备[{name._name}]已添加。")

    def remove_device(self,name):
        if name in self.data:
            del self.data[name]
            print(f"设备[{name}]已删除。")
        else:
            raise DeviceNotFoundError(f"没有找到设备[{name}]")

    def get_device(self):
        if name in self.devices:
            return self.devices[name]
        else:
            raise DeviceNotFoundError(f"没有找到设备 [{name}]")

# 测试代码
home_system = SmartHomeSystem()
light = Light("客厅灯光", brightness=50)
airconditioner = AirConditioner("客厅空调", temperature=22)
camera = SecurityCamera("前门摄像头", recording=True)

home_system.add_device(light)
home_system.add_device(airconditioner)
home_system.add_device(camera)

light.brightness = 75
airconditioner.temperature = 24
camera.status = True  # 没有这一句的话应该抛出异常
camera.recording = True
light.status = False

try:
    home_system.remove_device("厨房灯光")
except DeviceNotFoundError as e:
    print(e)
