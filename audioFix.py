import moviepy.editor as mp

output_video_path = 'output_slow_reverse_video.mp4'
input_video_path = 'testVideo.mp4'

modified_video_clip = mp.VideoFileClip(output_video_path)

original_audio_clip = mp.AudioFileClip(input_video_path)

final_video_clip = modified_video_clip.set_audio(original_audio_clip)

final_output_path = 'final_output_video.mp4'
final_video_clip.write_videofile(final_output_path, codec='libx264')

modified_video_clip.close()
original_audio_clip.close()
final_video_clip.close()
