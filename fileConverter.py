import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("test_video_output_temp.avi")
clip.write_videofile("test_video_output.mp4")