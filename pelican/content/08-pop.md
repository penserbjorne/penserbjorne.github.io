---
Title: Pop OS
Date: 2020-04-11
Modified: 2021-03-28
Tags: blog, penserbjorne
Keywords: blog, penserbjorne
Category: pop, linux
Author: penserbjorne
Summary: Pop OS
Lang: es-MX
Translation: false
Status: draft
---

-	Configurar `gedit`

-	Configurar disco extra
	-	Con disco bloqueado
		-	"Editar las opciones de cifrado"
	-	Con disco desbloqueado
		-	"Editar opciones de montaje"
	-	Creando enlace simbolico
		-	`ln -sf /mnt/extra/ ./extra`

-	Firefox
	-	Sync
	-	Configurar ruta de descarga a `extra`

-	Dropbox
	-	https://www.dropbox.com/install

-	Drive
	-	Añadir cuenta mediante GNOME

-	KeePassXC
	-	`sudo apt install keepassxc`

-	Cryptomator
	-	https://cryptomator.org/downloads/
	-	Utilizar PPA
	-	Activar actualizaciones automaticas

-	WPS Office
	-	https://linux.wps.com/
	-	https://jixianzhao.github.io/2019-07-04-install-WPS-Office-Fonts

-	Steam
	-	`sudo apt install steam`
	-	Configurar
		-	`proton`
		-	Biblioteca externa
		-	Descargas

-	gamemode
	-	`sudo apt install gamemode gnome-shell-extension-gamemode`
	-	Activar extensión en gnome-shell
	-	https://extensions.gnome.org/extension/1852/gamemode/

-	OBS
	-	`sudo apt install obs-studio obs-plugins`
-	Signal
	-	`sudo apt install signal-desktop`
	-	https://signal.org/download/

-	Telegram
	-	`sudo apt install telegram-desktop`
	-	Configurar carpeta de descargas

-	Calibre
	-	https://calibre-ebook.com/download_linux

-	Spotify
	-	`sudo apt install spotify-client`

-	EDA
	-	Referencia a la entrada correspondiente

-	VPN
	-	Por ahora TunnelBear
	-	https://www.tunnelbear.com/blog/linux_support/

-	git
	-	`git config --global user.name "John Doe"`
	-	`git config --global user.email johndoe@example.com`

-	VirtualBox
	-	`sudo apt install virtualbox virtualbox-ext-pack`
	-	https://www.kali.org/docs/virtualization/

-	OpenShot
	-	PPA
	-	https://www.openshot.org/ppa/
---

https://extensions.gnome.org/extension/1852/gamemode/
https://extensions.gnome.org/extension/7/removable-drive-menu/

SwapFaq Ubuntu
https://help.ubuntu.com/community/SwapFaq

Enable Hibernation on Pop OS
https://abskmj.github.io/notes/posts/pop-os/enable-hibernate/

Crear archivo swap en linux
https://itsfoss.com/create-swap-file-linux/#comments

Extension de hibernar en gnome
https://extensions.gnome.org/extension/755/hibernate-status-button/

Audio despues de hibernar
-	https://rtfm.co.ua/en/linux-no-sound-after-suspend-sleep-solution/
	-	https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/issues/766#note_490045
-	https://askubuntu.com/questions/1187835/only-getting-dummy-output-audio-after-resuming-kubuntu
-	https://bbs.archlinux.org/viewtopic.php?id=252030

-	https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting#No_sound_after_resume_from_suspend
-	https://www.reddit.com/r/ProtonVPN/comments/i2f7j5/solution_to_reconnecting_protonvpn_after/

Firefox despues de hibernar
-	https://bugzilla.mozilla.org/show_bug.cgi?id=1506017#c17
