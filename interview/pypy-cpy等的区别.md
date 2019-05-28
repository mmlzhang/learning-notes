

1. Cython： Cython是让Python脚本支持C语言扩展的编译器，Cython能够将Python+C混合编码的.pyx脚本转换为C代码，主要用于优化Python脚本性能或Python调用C函数库。

2. Pypy：Pypy最重要的一点就是Pypy集成了JIT。同时针对CPython的缺点进行了各方面的改良，性能得到很大的提升。了解JIT技术的人都应该对Pypy很有好感。Pypy的优点是对纯Python项目兼容性极好，几乎可以直接运行并直接获得性能提升（官方宣称为6.3倍……但是实际上没感觉有这么多）；缺点是对很多C语言库支持性不好，Pypy社区一直有相关讨论。

3. Numba：Numba是一个库，可以在运行时将Python代码编译为本地机器指令，而不会强制大幅度的改变普通的Python代码

通用性：在三个方案中，Cython和Numba的兼容性都非常好，而Pypy对于部分库的支持较差（如Numpy，Scipy）。

速度：这三种方案的速度相差不大，通常来说Cython要快于Pypy，尤其是对于部分C扩展。Pypy要快于Numba，但针对于纯数值计算的工作，Numba甚至还要快于Cython。

易用性：易用性最好的无疑是Pypy，Pypy是Python的解释器，我们针对纯Python使用Pypy，除了Pypy不支持的部分库外，不需要进行任何改动。然后是Numba，Numba的基本使用方法就是给函数加一个装饰器，易用性也很高，最后是Cython，因为Cython中需要使用Python+C混合编码，如果需要移植，代价会很大。

**总结：**Pypy是非常理想的Python解释器，最大的瑕疵就是对部分库的兼容问题。Cython是一种Python + C的便利性组合，转为C编译的扩展执行效率非常高，但使用相对麻烦，移植CPython项目代价较高。Numba更适合针对性优化，效率高，并且不会大幅度的改变普通的Python代码。