def extract_scene_name(element):
    scene = element.strong.text
    return scene


def extract_username(element):
    username = element.find_all("td")[1].span.text
    return username


def extract_size(element):
    size = element.find_all("td")[5].text
    return size


def extract_frames_number(element):
    frames_str = element.find(attrs={"class": "sr-only"}).text
    frames_cut_location = (frames_str.find("/") + 2)
    frames = frames_str[frames_cut_location:]
    return frames


def extract_enabled_devices(element):
    devices = element.find_all("td")[4].find_all("img")
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
