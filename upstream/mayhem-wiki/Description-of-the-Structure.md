# In this section
- [[At-first-glance|At First Glance]]
- [[Boot-Process|Boot Process]]
- [[Firmware-Architecture|Firmware Architecture]]
- [[Persistent-Memory|Persistent Memory]]
- [[ChibiOS-Notes|ChibiOS Notes]]

# Pseudo software side map
![image](https://github.com/user-attachments/assets/02b06812-d872-4272-8775-15eab2ebe8b1)


# Side notes
Note that it's not a real Vinn plot, which means:
![image](https://github.com/user-attachments/assets/29350148-ad4b-442c-a247-2116df264831)



# DrawIO xml file
```xml
<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0" version="26.0.10">
  <diagram name="第 1 页" id="H0zMpU18Cr5ldHpvN_dp">
    <mxGraphModel dx="1833" dy="576" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="mGF7w5FvqKM16RAacszP-1" value="&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;PortaPack&lt;/font&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="50" y="50" width="260" height="460" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-2" value="&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 39px;&quot;&gt;HackRF&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; &lt;br&gt;&lt;/font&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="370" y="50" width="280" height="460" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-3" value="&lt;font style=&quot;font-size: 14px;&quot;&gt;SDCard&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="70" y="80" width="220" height="260" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-4" value="&lt;font style=&quot;font-size: 21px;&quot;&gt;External and standalone apps&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#a20025;fontColor=#ffffff;strokeColor=#6F0000;" vertex="1" parent="1">
          <mxGeometry x="85" y="230" width="190" height="90" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-5" value="&lt;font style=&quot;font-size: 27px;&quot;&gt;Blob and resources files&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e3c800;fontColor=#000000;strokeColor=#B09500;" vertex="1" parent="1">
          <mxGeometry x="80" y="90" width="200" height="100" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-6" value="&lt;font style=&quot;font-size: 19px;&quot;&gt;5M40Z/AG256 CPLD bitstream &quot;firmware&quot;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="62.5" y="410" width="235" height="80" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-10" value="&lt;font style=&quot;font-size: 20px;&quot;&gt;Xilinx CPLD firmware&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcc99;strokeColor=#36393d;" vertex="1" parent="1">
          <mxGeometry x="390" y="410" width="240" height="80" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-12" value="&lt;font style=&quot;font-size: 22px;&quot;&gt;ESP32 plugin firmware (optional)&lt;br&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#647687;fontColor=#ffffff;strokeColor=#314354;" vertex="1" parent="1">
          <mxGeometry x="-190" y="50" width="190" height="460" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-14" value="&lt;div&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;1MB SPI flash&lt;/font&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#76608a;fontColor=#ffffff;strokeColor=#432D57;" vertex="1" parent="1">
          <mxGeometry x="390" y="60" width="250" height="280" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-8" value="&lt;div&gt;&lt;font style=&quot;font-size: 17px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 17px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 17px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 17px;&quot;&gt;&lt;br&gt;&lt;/font&gt;&lt;/div&gt;&lt;div&gt;&lt;font style=&quot;font-size: 17px;&quot;&gt;Application layer firmware&lt;/font&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffff88;strokeColor=#36393d;" vertex="1" parent="1">
          <mxGeometry x="400" y="70" width="230" height="140" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-9" value="&lt;font style=&quot;font-size: 18px;&quot;&gt;Baseband firmwares&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d80073;fontColor=#ffffff;strokeColor=#A50040;" vertex="1" parent="1">
          <mxGeometry x="400" y="242.5" width="110" height="80" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-11" value="&lt;font style=&quot;font-size: 15px;&quot;&gt;ChibiOS runtime&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fa6800;fontColor=#000000;strokeColor=#C73500;" vertex="1" parent="1">
          <mxGeometry x="430" y="80" width="180" height="80" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-7" value="&lt;font style=&quot;font-size: 13px;&quot;&gt;Our slightly modified HackRF firmware&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#60a917;fontColor=#ffffff;strokeColor=#2D7600;" vertex="1" parent="1">
          <mxGeometry x="520" y="245" width="110" height="75" as="geometry" />
        </mxCell>
        <mxCell id="mGF7w5FvqKM16RAacszP-15" value="not touchable DFU software" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;gradientColor=#7ea6e0;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="540" y="350" width="90" height="40" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

```