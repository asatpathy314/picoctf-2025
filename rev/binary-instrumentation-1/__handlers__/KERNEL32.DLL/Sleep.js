/*
 * Auto-generated by Frida. Please modify to match the signature of Sleep.
 * This stub is currently auto-generated from manpages when available.
 *
 * For full API reference, see: https://frida.re/docs/javascript-api/
 */

defineHandler({
  onEnter(log, args, state) {
    // Log original sleep duration
    log(`Sleep(${args[0]})`);
    
    // Get backtrace
    const bt = Thread.backtrace(this.context, Backtracer.ACCURATE);
    log('Called from:');
    bt.forEach((addr, i) => {
      log(`${i}\t${addr}`);
    })
    args[0] = ptr(1); // Change to 1ms instead of the original long duration
  },
  
  onLeave(log, retval, state) {
    // Optional: Add any code to execute when the function returns
  }
});
