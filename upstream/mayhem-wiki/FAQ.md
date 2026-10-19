- Q: My device `never boot`/ `white screen`/ `black screen` after `upgrade firmware`/ `reset`/ `coin battery dead`/ `took out sdcard`.  
  > A: Check [Won't boot](Won't-boot) and [Config Menu](Config-Menu)  
- Q: Something is `abnormal`/ `crashed`/ `not working`/ `behaving unexpected`/ `Guru Meditation`
  > A: Try [Completely reset](Completely-reset), if not helps, try [Updating the Xilinx CPLD on hackrf board](Updating-the-Xilinx-CPLD-on-hackrf-board), if still not helps, [report an issue on GitHub](https://github.com/portapack-mayhem/mayhem-firmware/issues/new/choose).  
- Q: `no splash screen displayed`/`No time & date displayed`/ `touchscreen not working`/ `status bar icon disappeared`/ `backlight timeout abnormal`/ `encoder dial abnormal`  
  > A: It's an option in settings, go check settings.  
- Q: It says `xxx missing`/ `can't find xxx`/ `xxx read error`/ `xxx is outdated` or you `can't see xxx`
  > A: Make sure you correctly put the sdcard contents matching your firmware version.    
- Q: There's an unexpected spike on my waterfall/ IQ/ spectrum  
  > A: It's either a [DC offset](https://hackrf.readthedocs.io/en/latest/faq.html#what-is-the-big-spike-in-the-center-of-my-received-spectrum) or noise from power. For noise you can try to use inner battery to reduce. For DC offset you can do nothing with it.