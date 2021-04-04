# xinput

- 列出所有设备与状态,id
xinput list

- 根据设备id列出设备属性
xinput list-props 14

- 设置设备属性
xinput set-prop 14 317 0.55


> List available input devices, query information about a device and change input device settings.

- List all input devices:

`xinput list`

- Disconnect an input from its master:

`xinput float {{id}}`

- Reattach an input as slave to a master:

`xinput reattach {{id}} {{master_id}}`
