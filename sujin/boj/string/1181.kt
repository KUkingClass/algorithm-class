
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val bw = System.`out`.bufferedWriter()

    val n = readLine().toInt()
    val words = mutableSetOf<String>()
    bw.use { w ->
        repeat(n) {
            words.add(readLine())
        }

        // sol 1
        val result = words.sortedWith { a, b ->
            when {
                a.length > b.length -> 1
                a.length == b.length -> when {
                    a > b -> 1
                    else -> -1
                }
                else -> -1
            }
        }

        // sol 2
        val result = words.sortedWith(
            compareBy (
                { it.length },
                { it }
            )
        )

        result.forEach {
            w.write("$it\n")
        }

    }
}


