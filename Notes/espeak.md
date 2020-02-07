# 中文
espeak "这是什么" -v zh

# 振幅
-a <integer>
           Amplitude, 0 to 200, default is 100

# 词间隙
-g <integer>
           Word gap. Pause between words, units of 10mS at the default speed

# 每分钟文字速度
-s <integer>
           Speed in words per minute, 80 to 450, default is 175

# 

# espeak

> Uses text-to-speech to speak through the default sound device.

- Speak a phrase aloud:

`espeak "I like to ride my bike."`

- Speak a file aloud:

`espeak -f {{filename}}`

- Save output to a WAV audio file, rather than speaking it directly:

`espeak -w {{filename.wav}} "It's GNU plus Linux"`

- Use a different voice:

`espeak -v {{voice}}`
