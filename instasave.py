import instaloader

def download_instagram_post(url):
    # Create an Instaloader instance
    loader = instaloader.Instaloader()

    try:
        # Retrieve media details
        post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 2)[-2])

        # Download the image
        loader.download_post(post, target='.')
        print(f"Image downloaded successfully: {post.url}")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

# Example usage
instagram_post_url = "https://www.instagram.com/p/C0UzPscymB1/?img_index=1"
download_instagram_post(instagram_post_url)
