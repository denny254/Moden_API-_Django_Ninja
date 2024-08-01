from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from devices.schemas import DeviceSchema, LocationSchema, DeviceCreateSchema
from devices.models import Device, Location


app = NinjaAPI()

@app.get("/devices", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

@app.get('devices/{slug}/', response=DeviceSchema)
def get_devices(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device 

@app.get("/locations", response=list[LocationSchema])
def get_devices(request):
    return Location.objects.all()

@app.post("devices/", response=DeviceCreateSchema)
def create_device(request, device: DeviceCreateSchema):
    device_data = device.model_dump()
    device_model = Device.objects.create(**device_data)
    return device_model