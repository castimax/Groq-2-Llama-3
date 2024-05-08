Manual de configuración y ejecución del chatbot
Requisitos previos

Python 3.7 o superior
Cuenta de Groq
Cuenta de Hugging Face (para el modelo Llama)

Pasos de configuración

Clonar el repositorio:

Abre una terminal o línea de comandos.
Navega hasta el directorio donde deseas clonar el repositorio.
Ejecuta el siguiente comando para clonar el repositorio:
git clone https://github.com/tu-usuario/nombre-del-repositorio.git



Crear y activar un entorno virtual (opcional pero recomendado):

Navega hasta el directorio del repositorio clonado:
cd nombre-del-repositorio

Crea un nuevo entorno virtual:
python -m venv venv

Activa el entorno virtual:

En Windows:
venv\Scripts\activate

En macOS y Linux:
source venv/bin/activate





Instalar las dependencias:

Con el entorno virtual activado, ejecuta el siguiente comando para instalar las dependencias:
pip install -r requirements.txt



Obtener la clave de API de Groq:

Ve a la página de inicio de sesión de Groq: https://groq.com/login
Inicia sesión en tu cuenta de Groq o crea una nueva cuenta si no tienes una.
Una vez iniciada la sesión, ve a la sección de configuración de tu cuenta.
Busca la opción para generar o ver tu clave de API.
Copia la clave de API de Groq.


Obtener la clave de API de Hugging Face:

Ve a la página de inicio de sesión de Hugging Face: https://huggingface.co/login
Inicia sesión en tu cuenta de Hugging Face o crea una nueva cuenta si no tienes una.
Una vez iniciada la sesión, ve a la sección de configuración de tu cuenta.
Busca la opción para generar o ver tu token de acceso.
Copia el token de acceso de Hugging Face.


Configurar las variables de entorno:

En el directorio raíz del repositorio, crea un nuevo archivo llamado .env.
Abre el archivo .env en un editor de texto.
Agrega las siguientes líneas al archivo, reemplazando TU_CLAVE_API_GROQ y TU_TOKEN_ACCESO_HUGGING_FACE con las claves correspondientes que obtuviste en los pasos anteriores:
GROQ_API_KEY=TU_CLAVE_API_GROQ
HUGGING_FACE_API_TOKEN=TU_TOKEN_ACCESO_HUGGING_FACE

Guarda y cierra el archivo .env.



Pasos de ejecución

Ejecutar la aplicación FastAPI:

En una terminal o línea de comandos, navega hasta el directorio del repositorio.
Asegúrate de tener el entorno virtual activado.
Ejecuta el siguiente comando para iniciar la aplicación FastAPI:
uvicorn main:app --reload

La API estará disponible en http://localhost:8000.


Ejecutar la aplicación Streamlit:

Abre otra terminal o línea de comandos.
Navega hasta el directorio del repositorio.
Asegúrate de tener el entorno virtual activado.
Ejecuta el siguiente comando para iniciar la aplicación Streamlit
streamlit run streamlit_app.py

Se abrirá una ventana del navegador con la interfaz de usuario de Streamlit.


Interactuar con el chatbot:

En la interfaz de usuario de Streamlit, ingresa tu pregunta en el campo de texto provisto.
Haz clic en el botón "Obtener respuesta" para enviar la pregunta al chatbot.
El chatbot procesará la pregunta y mostrará la respuesta generada junto con el contexto relevante.

¡Eso es todo!
