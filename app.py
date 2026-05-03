import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)


with st.sidebar:
    st.image("bajo-control.jpeg")

        


broker="157.230.214.127"
port=1883
client1= paho.Client("cliente_amadeus_10229")
client1.on_message = on_message



st.title("MQTT para enviar cosas en vez de recibirlas")

st.text("Unas aclaraciones... Para que funcione, el cliente NO puede ser el mismo que el de wokwi, pero el topico de subscripcion si")

st.text("Ahora una pequeña explicación de como funciona... Resulta que si le das a Encender la luz, y tambien si puedes escoges un valor en el slider, y le das al boton de enviar, tu valor se enviara a un MQTT para girar un motor en wokwi y encender una luz o apagarla")



if st.button('Encender la luz'):
    act1="ON"
    client1= paho.Client("cliente_amadeus_10229")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_sinosequees", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Apagar la luz'):
    act1="OFF"
    client1= paho.Client("cliente_amadeus_10229")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_sinosequees", message)
  
    
else:
    st.write('')

values = st.slider('Aquí puedes seleccionar el valor a enviar',0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor', type="primary"):
    client1= paho.Client("cliente_amadeus_10229")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("cmqtt_analogocreo", message)
    
 
else:
    st.write('')




