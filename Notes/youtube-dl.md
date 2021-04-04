# youtube-dl
youtube-dl --proxy "socks5://127.0.0.1:1080" -f 'bestvideo[height<=720]' 
# 指定最好视频格式
youtube-dl -f 'bestvideo[height<=720]'

# proxy
youtube-dl --proxy "socks5://127.0.0.1:1080"


# playlist
## 只列出信息
--flat-playlist

## 指定
--playlist-start NUMBER          Playlist video to start at (default is 1)

--playlist-end NUMBER            Playlist video to end at (default is last)

--playlist-items ITEM_SPEC       Playlist video items to download. Specify
                                 indices of the videos in the playlist
                                 separated by commas like: "--playlist-items
                                 1,2,5,8" if you want to download videos
                                 indexed 1, 2, 5, 8 in the playlist. You can
                                 specify range: "--playlist-items
                                 1-3,7,10-13", it will download the videos
                                 at index 1, 2, 3, 7, 10, 11, 12 and 13.

> Download videos from YouTube and other websites.

- Download a video or playlist:

`youtube-dl {{https://www.youtube.com/watch?v=oHg5SJYRHA0}}`

- Download the audio from a video and convert it to an MP3:

`youtube-dl -x --audio-format {{mp3}} {{url}}`

- Download video(s) as MP4 files with custom filenames:

`youtube-dl --format {{mp4}} --output {{"%(title) by %(uploader) on %(upload_date) in %(playlist).%(ext)"}} {{url}}`

- Download a video and save its description, metadata, annotations, subtitles, and thumbnail:

`youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail {{url}}`

- From a playlist, download all "Let's Play" videos that aren't marked "NSFW" or age-restricted for 7 year-olds:

`youtube-dl --match-title {{"let's play"}} --age-limit {{7}} --reject-title {{"nsfw"}} {{playlist_url}}`
