fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val bw = System.`out`.bufferedWriter()

    val (n, m) = readLine().split(" ").map { it.toInt() }
    val dna = mutableListOf<String>()

    var answer = ""
    var dist = 0

    bw.use { w ->

        repeat(n) {
            dna.add(readLine())
        }

        for (i in 0 until m) {
            val count = mutableMapOf<Char, Int>('A' to 0, 'T' to 0, 'G' to 0, 'C' to 0)

            for (j in 0 until n) {
                count[dna[j][i]] = count[dna[j][i]]!!.plus(1)
            }

            val (nucleo, cnt) = count.toList().sortedWith(
                compareBy(
                    { -(it.second) }, // 빈도수 내림차순 정렬
                    { it.first } // 사전순 오름차순 정렬
                )
            )[0]

            answer += nucleo
            dist += (n - cnt)
        }

        w.write("$answer\n$dist")
    }
}
