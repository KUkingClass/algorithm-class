
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val bw = System.`out`.bufferedWriter()

    val n = readLine().toInt()

    // sol1
    var result1 = 0

    bw.use { w ->
        repeat(n) {
            val word = readLine()

            var switch = 1
            val history = mutableListOf<Char>(word[0])

            for(i in 1 until word.length) {
                if(word[i-1] != word[i])
                    switch++

                if(!history.contains(word[i]))
                    history.add(word[i])
            }

            if(switch == history.size)
                result1++
        }

        w.write("$result1")
    }


    // sol2
    var result2 = n
    var alpha: BooleanArray

    bw.use { w ->
        repeat(n) {
            alpha = BooleanArray(26) { false }
            val word = readLine()
            alpha[word[0] - 'a'] = true

            for(i in 1 until word.length) {
                if(word[i-1] != word[i]) { // 다르지만
                    if(alpha[word[i] - 'a']) { // 이미 존재
                        result2--
                        break
                    }
                }
                alpha[word[i] - 'a'] = true
            }
        }
        w.write("$result2")
    }

}


