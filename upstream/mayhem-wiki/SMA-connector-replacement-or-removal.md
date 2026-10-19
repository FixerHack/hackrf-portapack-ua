> [!NOTE]  
> It is a good idea to protect the antenna connectors with a [silicone cover](https://www.aliexpress.com/item/33027991367.html?channel=twinner) 

The antenna connectors on the HackRF board are the `18.5 mm` variant available [here](https://s.click.aliexpress.com/e/_DEfOQ85).

Notice that you _could_ fit the `SMA-KE 18.5mm` variant, but it will be not the perfect fit for the type of pcb mount used in originally.

![image](https://user-images.githubusercontent.com/1091420/233613253-7a1d1949-f2f6-4c1d-be40-eaa1fa750ba4.png)

# Replacing a broken connector

1. Desolder the original, use enough flux (i.e. [this "self cleaning" variant](https://s.click.aliexpress.com/e/_DEfOQ85)) and fresh solder. If there is parts of the SMA connector still there, it might be more difficult to remove because the thermal mass. 

![image](https://user-images.githubusercontent.com/1091420/233613342-dfb284ee-b9ea-4851-8bed-b1313042632f.png)

2. Clean the pads

3. Place the new one. It will be very tight. Align it correctly

![image](https://user-images.githubusercontent.com/1091420/233613467-ce3a2e5b-7390-459d-939c-17e6cb0d34b4.png)

4. Solder and clean the residual flux

![image](https://user-images.githubusercontent.com/1091420/233613588-ca1efaf2-ab51-4c38-9fbb-e4e7f345765f.png)



# Removing a connector

You may want to remove the bottom sma connectors if you dont use them, or you may have a damaged connector that you need to remove before replacing it.
This is a simple way to do that without risk of damaging your PCB.

If you only want to remove the connector, all you need is a small file, preferably one that has a knife-like edge, it will make it easier.

Note that im using a random pcb i had lying around for this demonstration.

![sma 1](https://github.com/user-attachments/assets/e57df8e3-7d6f-49e5-83af-1735f7fd00b1)

1. Use your file to file down the pins holding the connector almost all the way down.


![sma 2](https://github.com/user-attachments/assets/8d0c5d46-3336-4414-921e-9ae1ae23232f)

2. Now flip the board over and do the same on the other side.

![sma 3](https://github.com/user-attachments/assets/59f346c1-74a7-4b7d-991b-e18b7c4d6aa9)

3. At this point you want to rock the plug up and down lightly, it should break off. You may have to file the pins a little bit more if it doesnt break off with very light force.

![sma 4](https://github.com/user-attachments/assets/9e4029f4-8771-409b-aa82-cda29968680f)

4. Once the connector is removed, you can de-solder the remaining pins one by one, or just clean up the dust and leave it as it is, if you are just removing the CLCK IN/OUT connectors.

![sma 5](https://github.com/user-attachments/assets/45217e0a-0f16-4654-a356-3186fef8377c)

