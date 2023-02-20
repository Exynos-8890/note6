using System;
using System.Diagnostics;
using System.Threading;

class Program {

    static Func<int> GetRand7FromRand8(Func<int> rand8) {
        UInt64 buffer = default;
        int count = 0;
        return () => {
            if (count <= 0) {
                for (; ; ) {
                    UInt64 t = 0;
                    for (var i = 0; 15 > i; ++i) {
                        var r = rand8();
                        Debug.Assert(1 <= r && r <= 8);
                        r -= 1;
                        t *= 8;
                        t += (uint)r;
                    }
                    if (t < /* 7 ^ 16 */33232930569601) {
                        count = 15;
                        buffer = t;
                        goto L;
                    }
                }
            }
            --count;
        L:;
            var q = buffer / 7;
            var result = (int)(buffer - q * 7);
            buffer = q;
            result += 1;
            Debug.Assert(1 <= result && result <= 7);
            return result;
        };
    }

    static Func<int> GetRand7FromRand8Naive(Func<int> rand8) {
        return () => {
            int result;
            while ((result = rand8()) == 8) ;
            return result;
        };
    }

    static void Main(string[] args) {
        Thread.CurrentThread.Priority = ThreadPriority.Highest;
        Func<int> rand8 = static () => System.Security.Cryptography.RandomNumberGenerator.GetInt32(1, 8 + 1);

        var loop_count = 1000000;
        Console.WriteLine($@"测试（预热）{nameof(GetRand7FromRand8)} ...");
        RunTest(rand8, GetRand7FromRand8, loop_count);

        Console.WriteLine($@"测试（预热）{nameof(GetRand7FromRand8Naive)} ...");
        RunTest(rand8, GetRand7FromRand8Naive, loop_count);

        loop_count = 100000000;
        Console.WriteLine($@"测试 {nameof(GetRand7FromRand8)} ...");
        RunTest(rand8, GetRand7FromRand8, loop_count);

        Console.WriteLine($@"测试 {nameof(GetRand7FromRand8Naive)} ...");
        RunTest(rand8, GetRand7FromRand8Naive, loop_count);

        static void RunTest(Func<int> rand8, Func<Func<int>, Func<int>> getRand7FromRand8, int loopCount) {
            var sw = new Stopwatch();
            var rand7 = getRand7FromRand8(rand8);
            Span<int> counts = stackalloc int[7];
            sw.Restart();
            for (var i = 0; loopCount > i; ++i) {
                var r = rand7();
                ++counts[r - 1];
            }
            sw.Stop();
            for (var r = 1; r <= 7; ++r) {
                var count = counts[r - 1];
                Console.WriteLine($@"抽中结果 {r}：{count,8} 次。频率：{100.0 * count / loopCount:#0.00} %。");
            }
            Console.WriteLine($@"耗时：{sw.Elapsed.TotalSeconds:#0.000} 秒。");
            Console.WriteLine();
        }
    }
}