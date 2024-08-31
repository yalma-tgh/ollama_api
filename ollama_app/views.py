from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import ollama

@api_view(['POST'])
def ollama_chat(request):
    try:
        # Extract the message from the request data
        message = request.data.get('message', '')

        # Interact with the Ollama model
        response = ollama.chat(model='gemma2:2b', messages=[
            {
                'role': 'user',
                'content': message,
            },
        ])

        # Return the response from the model as JSON
        return Response({'response': response['message']['content']}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
