
# WeConnect - Real-time Chat Application

## Project Overview

**WeConnect** is a minimalist yet functional chat application designed to allow users to connect and communicate with each other in real-time. The application supports both individual and group conversations, user management, and essential chat functionalities.

## Objective

To create a secure and scalable communication platform that provides users with a clean and user-friendly interface for real-time messaging. The initial version (MVP) will focus on core features with room for future enhancements.

## Core Features

### 1. Accounts App (User Management)
- **User Registration:**
  - Users can sign up using an email address, username, and password.
  - Email verification for account activation.
  
- **User Authentication:**
  - Secure login/logout functionality.
  - Password recovery/reset mechanism via email.
  
- **User Profiles:**
  - Basic profile information (username, email, profile picture).
  - Ability to update profile information.
  
- **User Status:**
  - Set and display online/offline status.
  - Option to set a custom status message.
  
- **Friend Requests/Connections:**
  - Send and accept friend requests.
  - View a list of friends/connections.

### 2. Chat App (Messaging System)
- **One-on-One Chat:**
  - Real-time messaging between two users using WebRTC.
  - Message delivery status (sent, delivered, seen).
  - Basic text formatting (bold, italics, etc.).
  
- **Group Chat:**
  - Create and manage group chats.
  - Add or remove members from a group.
  - Group admins with the ability to moderate the chat.
  
- **Media Sharing:**
  - Send and receive images, videos, and files within chats.
  
- **Chat Notifications:**
  - Real-time notifications for new messages.
  - Customizable notification settings (mute, do not disturb).
  
- **Chat History:**
  - Persist chat history in the database.
  - Ability to view and search past conversations.

### 3. Real-time Communication
- **WebRTC Integration:**
  - Utilize WebRTC for real-time communication, enabling live chat and potentially voice/video features in the future.
  
- **WebSockets:**
  - Implement Django Channels for real-time messaging using WebSockets.
  - Ensure messages are delivered instantly with real-time updates.

## Technical Stack

- **Backend:**
  - Django (Python)
  - Django REST Framework (for APIs)
  - Django Channels (for WebSockets and real-time communication)
  
- **Frontend:**
  - HTML/CSS/JavaScript (for a minimal but functional UI)
  - Bootstrap or Tailwind CSS (for responsive design)
  - React.js or Vue.js (optional, for a more dynamic frontend experience)
  
- **Database:**
  - PostgreSQL (Primary database for user accounts, chat history, etc.)
  - Redis (for caching and real-time data handling)
  
- **Authentication & Security:**
  - Django Allauth or custom authentication system.
  - JWT (JSON Web Tokens) or Django sessions for secure authentication.
  - HTTPS for secure communication.

## Project Milestones

1. **Initial Setup & User Management:**
   - Set up Django project with required apps (Accounts, Chat).
   - Implement user registration, login, and profile management.
  
2. **Basic Chat Functionality:**
   - Implement one-on-one chat with real-time messaging.
   - Create a basic UI for individual chats.
  
3. **Group Chat & Media Sharing:**
   - Enable group chat functionality.
   - Add support for media sharing within chats.
  
4. **Notifications & Chat History:**
   - Integrate real-time notifications for incoming messages.
   - Implement chat history with search functionality.
  
5. **Testing & Deployment:**
   - Perform unit and integration testing.
   - Set up a production environment and deploy the application.

## Future Enhancements (Beyond MVP)

- **Voice/Video Calls:** Expand WebRTC integration to support voice and video calls.
- **Advanced Search:** Implement advanced search features within chats (by keywords, dates, etc.).
- **Custom Emojis/Stickers:** Allow users to send custom emojis or stickers in chat.
- **Status Updates:** Allow users to post status updates or stories visible to their connections.
- **Mobile App:** Develop a mobile version of the application using React Native or Flutter.

## Conclusion

WeConnect is designed to be a secure, real-time communication platform with a minimalist design and essential features. It provides a solid foundation for future enhancements, ensuring scalability and ease of use.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/WeConnect.git
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django REST Framework - For creating robust APIs.
- Django Channels - For handling WebSockets and real-time communication.
- WebRTC - For enabling real-time chat capabilities.
- Bootstrap/Tailwind CSS - For providing responsive design components.
- All open-source contributors and developers who made this project possible.

