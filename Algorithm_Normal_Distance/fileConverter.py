import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("Algorithm/test_video_output.avi")
clip.write_videofile("Algorithm/test_video_output.mp4")