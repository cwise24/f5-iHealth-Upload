# f5-iHealth-Upload
Python script (`qk.py`) will upload multiple files from directory <br />
The `qkvw.yml` play will use host vars from Ansible to get the alias name of the target, in this example *BigIp13* <br />
Upload Qkview using Ansible play and the iHealth API (thanks to python). Below is the DevCentral article covering the [iHealth API](https://clouddocs.f5.com/api/ihealth/)
<br />
From this example you can edit the user_id and user_secret like: <br />
`payload = {'user_id':'j.smith@example.com', 'user_secret':'S3cretP@ssword'}`
