
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val bw = System.`out`.bufferedWriter()

    bw.use { w ->
        val s = readLine()
        val p = readLine()

        w.write("${kmp(s, p)}")

    }
}

fun kmp(target: String, pattern: String): Int {
    val pi: IntArray = getPi(pattern)
    val n = target.length
    val m = pattern.length

    var j = 0
    for(i in 0 until n) {
        while(j > 0 && target[i] != pattern[j]) {
            j = pi[j-1]
        }

        if(target[i] == pattern[j]) {
            if(j == m - 1) {
                j = pi[j]
                return 1 // 부분 문자열
            }
            else {
                j++
            }
        }
    }
    return 0
}

fun getPi(pattern: String): IntArray {
    val m = pattern.length
    val pi = IntArray(size = m) { 0 }

    var j = 0
    for (i in 1 until m) {
        // 일치하는 문자 발생
        // 연속적으로 더 일치하지 않으면 j = pi[j-1]로 되돌려줌
        while(j > 0 && pattern[i] != pattern[j]) {
            j = pi[j-1]
        }
        if(pattern[i] == pattern[j]) {
            j++
            pi[i] = j
        }
    }
    return pi
}

