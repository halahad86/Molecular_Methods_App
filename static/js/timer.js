function timer() {
    window.onload = function () {
        var curCount = 0
            , timeBox = document.getElementById('time')
            , loopCheck = document.getElementById('loop')
            , counterDiv = document.getElementById('counter')
            , resetBtn = document.getElementById('reset')
            , startBtn = document.getElementById('start')
            , counterInt

        function updateCounter() {
            counterDiv.innerHTML = curCount
        }

        function reset() {
            startBtn.disabled = false
            document.getElementById("timerSound").load()
            curCount = parseInt(timeBox.value) || 0
            clearInterval(counterInt)
            updateCounter()
            counterDiv.style.color = '#fff'
        }

        function start() {
            reset()
            document.getElementById("timerSound").load()
            startBtn.disabled = true
            counterDiv.style.color = '#FAFBFB'
            counterInt = setInterval(function () {
                curCount--
                if (curCount == 0) {
                    document.getElementById("timerSound").play()
                    //window.alert("Time is up!")
                    $("#dialogTimer").dialog(
                        {   width: 300,
                            closeOnEscape: false,
                            draggable: true,
                            open: function () {
                                $('.ui-dialog-titlebar-close').removeClass("ui-dialog-titlebar-close").html('<span>X</span>');
                            }
                        }
                    );
                    $("#dialogTimeUp").text("Time is up !");


                }
                if (curCount < 0) {
                    if (!loopCheck.checked) {
                        clearInterval(counterInt)
                        reset()
                    } else {
                        curCount = parseInt(timeBox.value) || 0

                    }
                }
                updateCounter()
            }, 1000)
        }

        resetBtn.onclick = reset
        startBtn.onclick = start
        reset()
    }
}
