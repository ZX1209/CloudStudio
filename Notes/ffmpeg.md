# FFmpeg 常用的命令行参数如下。

-c：指定编码器
-c copy：直接复制，不经过重新编码（这样比较快）
-c:v：指定视频编码器
-c:a：指定音频编码器
-i：指定输入文件
-an：去除音频流
-vn： 去除视频流
-preset：指定输出的视频质量，会影响文件的生成速度，有以下几个可用的值 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。
-y：不经过确认，输出时直接覆盖同名文件。


# FFmpeg 的命令行参数非常多，可以分成五个部分。


$ ffmpeg {1} {2} -i {3} {4} {5}
上面命令中，五个部分的参数依次如下。

全局参数
输入文件参数
输入文件
输出文件参数
输出文件
参数太多的时候，为了便于查看，ffmpeg 命令可以写成多行。


$ ffmpeg \
[全局参数] \
[输入文件参数] \
-i [输入文件] \
[输出文件参数] \
[输出文件]

下面是一个例子。

## 快速截图 
> -ss 放在最前面
> 指定输出编码 -vcodec
[
	"ffmpeg",
	"-ss",
	"00:02:00.000",
	"-y",
	"-i",
	str(item),
	"-r",
	"1",
	"-vframes",
	"1",
	"-an",
	"-vcodec",
	"mjpeg",
	str(picOutBase / (str(item.stem) + ".jpg")),
	]

$ ffmpeg \
-y \ # 全局参数
-c:a libfdk_aac -c:v libx264 \ # 输入文件参数
-i input.mp4 \ # 输入文件
-c:v libvpx-vp9 -c:a libvorbis \ # 输出文件参数
output.webm # 输出文件
上面的命令将 mp4 文件转成 webm 文件，这两个都是容器格式。输入的 mp4 文件的音频编码格式是 aac，视频编码格式是 H.264；输出的 webm 文件的视频编码格式是 VP9，音频格式是 Vorbis。

如果不指明编码格式，FFmpeg 会自己判断输入文件的编码。因此，上面的命令可以简单写成下面的样子。


$ ffmpeg -i input.avi output.mp4

# 4.6 提取音频
有时，需要从视频里面提取音频（demuxing），可以像下面这样写。


$ ffmpeg \
-i input.mp4 \
-vn -c:a copy \
output.aac
上面例子中，-vn表示去掉视频，-c:a copy表示不改变音频编码，直接拷贝。

# 参考
http://www.ruanyifeng.com/blog/2020/01/ffmpeg.html

# ffmpeg

> Video conversion tool.

- Extract the sound from a video and save it as MP3:

`ffmpeg -i {{video_filename}} -vn -ar 44100 -ac 2 -ab 192 -f mp3 {{sound.mp3}}`

- Convert frames from a video or GIF into individual numbered images:

`ffmpeg -i {{video_or_gif_filename}} {{image%d.png}}`

- Combine numbered images (image1.jpg, image2.jpg, etc) into a video or GIF:

`ffmpeg -f image2 -i {{image%d.jpg}} {{video.mpg_or_video.gif}}`

- Convert AVI video to MP4. AAC Audio @ 128kbit, Video @ 1250Kbit:

`ffmpeg -i {{in.avi}} -acodec libfaac -ab 128k -vcodec mpeg4 -b 1250K {{out.mp4}}`
