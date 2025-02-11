from django.db import models

class Package(models.Model):
    package_id = models.CharField(max_length=100, unique=True)  # 包裹ID
    status = models.CharField(max_length=100)  # 包裹状态，例如：待发货、运输中、已到达等
    current_location = models.CharField(max_length=255)  # 包裹当前位置
    destination = models.CharField(max_length=255)  # 包裹目的地

    def __str__(self):
        return self.package_id
