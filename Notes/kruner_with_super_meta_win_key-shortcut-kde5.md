Open KRunner with Windows/Meta key
We need to set Meta= under the group [ModifierOnlyShortcuts] in the file ~/.config/kwinrc, then reload kwin.
It's easier to use these commmands than doing it by hand.
Plasma 5.18 and above:
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch"
qdbus org.kde.KWin /KWin reconfigure

https://userbase.kde.org/Plasma/Tips#:~:text=Windows%2FMeta%20Key,-Open%20%E2%80%9CStart%20Menu&text=Feature%20has%20been%20added%20by,if%20another%20shortcut%20is%20assigned).