# main.py
import instaloader

def download_instagram_post(url, target_folder='.', progress_bar=None):
    loader = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 2)[-2])

        # Determine the total number of files to be downloaded (image or video)
        total_files = 1 if not post.is_video else 2

        # Configure progress bar
        if progress_bar:
            progress_bar["maximum"] = total_files
            progress_bar["value"] = 0

        if post.is_video:
            # Download video
            loader.download_post(post, target=target_folder)
            if progress_bar:
                progress_bar["value"] += 1

        # Download image
        loader.download_post(post, target=target_folder)
        if progress_bar:
            progress_bar["value"] += 1

        print("Download successful!")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")
