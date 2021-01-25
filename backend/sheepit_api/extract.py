class Extract:
    element = None

    def __init__(self, element):
        self.element = element

    def username(self):
        username = self.element.find_all("td")[1].span.text
        return username

    def scene_name(self):
        scene = self.element.strong.text
        return scene

    def size(self):
        size = self.element.find_all("td")[5].text
        return size

    def frames_number(self):
        frames_str = self.element.find(attrs={"class": "sr-only"}).text
        frames_cut_location = (frames_str.find("/") + 2)
        frames = frames_str[frames_cut_location:]
        return frames

    def enabled_devices(self):
        devices = self.element.find_all("td")[4].find_all("img")
        cpu = devices[0]["alt"]
        gpu = devices[1]["alt"]
        cpu_is_enabled = cpu.find("enabled") > 0
        gpu_is_enabled = gpu.find("enabled") > 0
        switch = {
            1: "CPU",
            2: "GPU",
            3: "CPU/GPU"
        }
        enabled_devices = switch.get(cpu_is_enabled + gpu_is_enabled * 2)
        return enabled_devices
