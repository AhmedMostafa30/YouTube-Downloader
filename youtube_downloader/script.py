from pytube import YouTube
# link = 'https://www.youtube.com/watch?v=Y_xB_maPsF8'
link = input("Enter the Link of the video: ")
video = YouTube(link)

# print(f"The Video title is:\n{video.title} \n----------------------------")
# print(f"The Video discription is:\n{video.description} \n----------------------------")
# print(f"The Video views are:\n{video.views} \n----------------------------")
# print(f"The Video rating is:\n{video.rating} \n----------------------------")
# print(f"The Video duration is:\n{video.length} seconds\n----------------------------")

# print(video.streams)

# for streams in video.streams:
#     print(streams)

# for streams in video.streams.filter(type="audio"):
#     print(streams)

# for streams in video.streams.filter(res="720p"):
#     print(streams)

# for streams in video.streams.filter(subtype="mp4"):
#     print(streams)

# print(video.streams.get_audio_only()) 
# print(video.streams.get_highest_resolution())
# print(video.streams.get_lowest_resolution())

def download_finished():
    print("Download Done Successfully!!")

choice = input("If you want to download the vedio as an audio press 1 else press any key:\n")
if choice == "1":
    video.streams.get_audio_only().download(output_path="C:/Users/ahmoc/Desktop")
else:
    video.streams.get_highest_resolution().download(output_path="C:/Users/ahmoc/Desktop")
# video.streams.get_audio_only().download(output_path="C:/Users/ahmoc/Desktop")
video.register_on_complete_callback(download_finished())