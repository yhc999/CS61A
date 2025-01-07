from operator import add, sub, mul, truediv

#CS61A: 2.4.9 约束传递 (Propagating Constraints)


# 理想气体状态方程:p * v = n * k * t 
# (通过玻尔兹曼常数 (k) 将理想气体的压力 (p)、体积 (v)、数量 (n) 和温度 (t) 联系起来)


# 华氏温度和摄氏温度之间的关系是：
# 9 * c = 5 * (f - 32)

def converter(c, f):
        """用约束条件连接 c 到 f, 将摄氏度转换为华氏度."""
        u, v, w, x, y = [connector() for _ in range(5)]
        multiplier(c, w, u)
        multiplier(v, x, u)
        adder(v, y, f)
        constant(w, 9)
        constant(x, 5)
        constant(y, 32)

def adder(a, b, c):
        """约束 a+b=c"""
        return make_ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
        """约束 a*b=c"""
        return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
        """常量赋值"""
        constraint = {}
        connector['set_val'](constraint, value)
        return constraint

def make_ternary_constraint(a, b, c, ab, ca, cb):
        """约束 ab(a,b)=c, ca(c,a)=b, cb(c,b)=a"""
        def new_value():
            av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
            if av and bv:
                c['set_val'](constraint, ab(a['val'], b['val']))
            elif av and cv:
                b['set_val'](constraint, ca(c['val'], a['val']))
            elif bv and cv:
                a['set_val'](constraint, cb(c['val'], b['val']))
        def forget_value():
            for connector in (a, b, c):
                connector['forget'](constraint)
        constraint = {'new_val': new_value, 'forget': forget_value}
        for connector in (a, b, c):
            connector['connect'](constraint)
        return constraint

def connector(name=None):
        """限制条件之间的连接器"""
        informant = None
        constraints = []
        def set_value(source, value):
            nonlocal informant
            val = connector['val']
            if val is None:
                informant, connector['val'] = source, value
                if name is not None:
                    print(name, '=', value)
                inform_all_except(source, 'new_val', constraints)
            else:
                if val != value:
                    print('Contradiction detected:', val, 'vs', value)
        def forget_value(source):
            nonlocal informant
            if informant == source:
                informant, connector['val'] = None, None
                if name is not None:
                    print(name, 'is forgotten')
                inform_all_except(source, 'forget', constraints)
        connector = {'val': None,
                     'set_val': set_value,
                     'forget': forget_value,
                     'has_val': lambda: connector['val'] is not None,
                     'connect': lambda source: constraints.append(source)}
        return connector

def inform_all_except(source, message, constraints):
        """告知信息除了 source 外的所有约束条件"""
        for c in constraints:
            if c != source:
                c[message]()


celsius = connector('Celsius')

fahrenheit = connector('Fahrenheit')

converter(celsius, fahrenheit)

celsius['set_val']('user', 25)

fahrenheit['set_val']('user', 212)