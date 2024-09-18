# Servicio de Correos Autoresponder  

Una aplicación web que permite mandar correos electronicos con contenido de Marketing para cualquier tienda online!

## Funcionalidades 

- Registro de email de los usuarios cuando visitan la web.
  
   ![news1](https://github.com/user-attachments/assets/8579fd53-3cb0-4bc6-b45a-66e934e01042)
  
- Envio de un correo electrónico al email del usuario despues de haberlo ingresado, se envia automaticamente
  
  ![news2](https://github.com/user-attachments/assets/275386cd-6f7e-4108-bc00-3415fc5ff309)
  
 Se envia con formato HTML creado desde el servidor donde se puede modificar al gusto de la tienda!
  ![news11](https://github.com/user-attachments/assets/0fd71a5d-0082-4348-8199-027d0a1baeff)

- Vista de una dashboard del estado de las diferentes POST NEWSLETTERS que se han creado
  
  ![news3](https://github.com/user-attachments/assets/2a047c82-9cb2-48a0-a50a-53cea502889b)

- Creación de nuevas Newsletters donde se llenan los campos title, subject, body
  Se envian a una o varias direcciónes de correo electrónico junto a su estado publish o Draft donde publish hace que se envie directaente al correo
  
  ![news4](https://github.com/user-attachments/assets/4a4e6811-4355-4991-9e76-a79dcfb3bcb8)

  ![news5](https://github.com/user-attachments/assets/9cbe974a-c9da-4ea0-b01f-3e30280a529b)

- Verificando el envio de una newsletters con el contenido creado desde la web de correos autoresponder
  
![news6](https://github.com/user-attachments/assets/e84f41a9-9b50-4fa5-be39-054f7a3a9f16)

- Desde la dashboard se puede ingresar a la newsletter para actualizar alguno de sus campos 

  ![news7](https://github.com/user-attachments/assets/b0bcccac-2af2-4265-89e1-db6ec8466133)

  ![news8](https://github.com/user-attachments/assets/398d6315-2a44-4a52-b618-35b4a2b3cfd6)

- Eliminar una newsletters desde la dashboard
  
  ![news9](https://github.com/user-attachments/assets/3a79e242-4320-487a-8533-00c5d7315733)

- No se puede ingresar con una dirección de correo repetida 

  ![news10](https://github.com/user-attachments/assets/46965ccd-af68-456d-bcec-a225a238d05e)


## Tecnologías 

**Backend:** 
  - Python version 3.11.0
  - Django version: 5.0.6
  - Django EmailMessage, integrado en Django


**Frontend:**
  - HTML5
  - Tailwind css
     
  
**Base de datos:** 
  - Sqlite3

**Servicios:**
  - SMTP de GOOGLE para el servidor de correos 
  

## Requisitos previos para utilizarla en tu entorno local:
 * Python y pip instalados
 * Un entorno virtual configurado
Instalación:
 * Clonar el repositorio: git clone https://github.com/lesterdavid31/Servicio_correos_autoresponder.git
 * Crear y activar el entorno virtual:
   python -m venv venv
source venv/bin/activate

 * Instalar las dependencias: pip install
  ~~~
   -r requirements.txt
   ~~~
 * Migrar la base de datos:
 ~~~
   python manage.py migrate
 ~~~

### **Pronto estára desplegado en la Nube**

