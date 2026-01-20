from captcha.audio import AudioCaptcha

audio = AudioCaptcha(voicedir='data/')
audio.write("1024","captcha.wav")