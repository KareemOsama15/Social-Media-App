import React, { useState, useRef } from 'react';
import axios from 'axios';

const CreatePost = () => {
  const [isCreatingPost, setIsCreatingPost] = useState(false);
  const [postContent, setPostContent] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const fileInputRef = useRef(null);

  const handleInputChange = (event) => {
    setPostContent(event.target.value);
  };

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSelectPhoto = () => {
    fileInputRef.current.click();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      console.log(postContent,selectedImage)
      const formData = new FormData();
      formData.append('content', postContent);
      formData.append('image', selectedImage);

      await axios.post('http://127.0.0.1:8000/api/posts/create/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Clear the input fields and hide the form
      setPostContent('');
      setSelectedImage(null);
      setIsCreatingPost(false);
    } catch (error) {
      console.error('Error creating post:', error);
      // Handle error
    }
  };

  return (
    <div className="relative">
      {isCreatingPost && (
        <div className="fixed top-0 left-0 w-full h-full bg-gray-800 opacity-50 z-50"></div>
      )}
      <div className="flex items-center justify-center m-auto relative">
        {isCreatingPost && (
          <div className="absolute top-1/2    bg-white p-8 rounded-lg w-full md:w-1/2 lg:w-1/3 z-50">
            <h3 className="text-center font-bold mb-3">Create Post</h3>
            <hr className="my-4"></hr>
            <textarea
              className="w-full h-40 border border-gray-300 rounded-md px-3 py-2 mb-4"
              placeholder="What's on your mind, Asmaa?"
              value={postContent}
              onChange={handleInputChange}
            />
            <input
              type="file"
              accept="image/*"
              onChange={handleImageChange}
              ref={fileInputRef}
              className="hidden"
            />
            <button
              className="flex bg-blue-500 text-white px-4 py-2 rounded-md mb-4 hover:bg-blue-600"
              onClick={handleSelectPhoto}
            >
              Add Photo
            </button>
            <div className="flex justify-center space-x-2">
              <button
                className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
                onClick={handleSubmit}
              >
                Post
              </button>
              <button
                className="bg-gray-200 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-300"
                onClick={() => setIsCreatingPost(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        )}
        <div className="flex w-full md:w-1/2 lg:w-1/2 bg-white p-8 rounded-lg">
          <img
            src="https://th.bing.com/th/id/OIP.WV-kmSwRhwiUgn6W74pxAAHaD4?rs=1&pid=ImgDetMain"
            alt="img-user"
            className="rounded-full w-16 h-16 mr-4"
          />
          <input
            type="submit"
            className="bg-gray-100 px-2 py-1 w-full rounded-full text-gray-500 cursor-pointer"
            value="What's on your mind, Asmaa?"
            onClick={(e) => {
              e.preventDefault();
              setIsCreatingPost(true);
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default CreatePost;
