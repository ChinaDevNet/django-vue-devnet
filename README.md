## 前言
受众人群：网络工程师、网工开发者以及网络运维领域从业人员
这有可能是一个极度难产或即将胎死腹中的平台，但我还是想谈谈一些个人看法……
随着NetDevOps的兴起，网工转型的开发者，依然需要面临很多现实问题。
比如：
1. 为了转型而需要投入的精力分配问题
2. 普遍网工转型的开发，代码能力成熟期需要较长的时间
3. 国外工具在国内经常出现水土不服的情况，各种问题颇为苦恼
4. 国内设备厂商在自动化方面进度缓慢，至今都没有一个大一统的标准协议，即使有，也只是套了一层皮。厂家间壁垒束之高阁。
5. 头部云厂商早就看透了这些，他们已经有了更好的解决方案，但，除了他们呢？

### 您是否有类似经历？
1. 你觉得构建一个相对完整的网络运维相关的平台，需要多久？
2. python、web框架、前后端中间件是否让你如临大敌，有担心过顾此失彼吗？
3. 能否在开发转型和网络运维找准平衡吗？
4. 掌握了很多开源工具，但用python将他们粘在一起的时候，总觉得差点意思？
5. 在埋头写bug的同时，是否有担心过，自己写的功能，可能一开始就不是最优解？
6. 接到新的需求的时候，发现原来写的代码过于死板不够灵活？
7. 开发出的功能，真的提高了运维的效率吗？ 如果没有，是需求、技术分析、产品思维的缺失吗？如何能够少走一些弯路？
8. 感受过重构一个功能的痛苦吗？
9. 国外的NetDevOps相关的工具，拿到国内，总是差点意思？
10. 国产化设备的自动化能力什么时候能够跟上啊？
11. 是否为平台架构的最优解苦恼？
12. 好不容易屏蔽了多家厂商在采集与下发上的差异，缺发现业务逻辑还是不够灵活？
13. 如何评估平台效能？
14. 前端！前端！还是TMD前端！
15. 自研的平台是否和自身IT业务深度绑定无法自拔？当你想做功能解耦的时候却发现早已经是一团乱麻
16. 会写脚本不等于会写平台，如果用脚本的思维去写平台，无异于管杀不管埋，如果再加上蹩脚的代码水平，要么给自己挖坑，要么给后人留坑(很容易魔性循环)


### 初衷想法。
1. 一个契合企业自身网络运维环境的网络运维平台，从0到1易，从1往上难。
2. 个人理解网工是最懂他们想要的功能，但网工转型的开发，需要很强的综合实力，抛开网络本身，还需要产品力、开发力(前后端一体)、架构力等等。
3. 这个行业已经足够细分，单网工和单开发都是很难在两三年内干成或者说实际产品很难让网工用的飞起。
4. 因为足够细分，对人员的要求较高，所以我们很难找到合适的人来干这件事(如果对JD做取舍，团队综合成本会显著增加)。
5. 除了头部大厂，行业内各自平台的南向接口借助开源生态已经解决了很多实际问题，但网工开发者们的代码质量堪忧且与自身业务深度绑定……
6. 如果真的陷入写bug修bug的循环，将很难有精力去关注网络运维这件事本身(毕竟单单学好网络就极不容易了)。


从行业的整体发展以及自身的感受来说，网络运维平台本身就可以拆解为两个不同视角的平台：网络自动化平台 和 与自身业务深度绑定的运维平台
而网络自动化平台，应该是能够将通用性非常强的南向适配能力集大成的独立平台。

此处应有图，后面有空再补

### 总体方向
1. 平台的前期功能将重点围绕行业内通用的功能。
2. 借助开源完善自动化的平台底座，让网工能有更多精力放在网络运维自身和专注其上层业务平台的编排更贴合企业自身IT环境需求。
3. 缓解NetDevOps细分领域上人才队伍的青黄不接，毕竟会网络又懂开发的，要么招不到，要么很难招且水平差异较大，如果平台能成，我们真的只需要简单的JD。
4. 本身NetDevOps和网工这两条路都很难走，很多都选择了转型……。

### 亮点
1. 我们需要把网工开发者们从繁杂的事务中给予一点解脱，比如中间件、数据库、前端、平台优化部署等等这些不算核心但又不得不做的事务陷入进去很容易舍本逐末，我们可以提供相对完善的开箱方案，使网工开发者能有更多的精力放在网络运维效能提升上。比如专注于编排自己的playbook、专注于数据的分析和运营、专注于用SRE的思想提高网络可靠性等等。
2. 国外的一些同类产品，大多以开发者交差的心态去做某一个功能，其实我们只需站在一个网工的日常工作去思考，通过合理的代码逻辑+通用化场景，先从配置备份入手。


### 平台特点
我们希望做一个国内版的netbox，NetDevOps领域的Tower。
那么，我们要解决哪些问题呢？ 亮点在哪里？
1. 南向接口： 从专业开发的角度，构建一个扩展性足够灵活的南向接口适配层。
2. 统一数据模型： 我们将统一网络设备常用表项的各个键值，做到厂商无关。
3. 自动化功能：很多同质化的产品，往往过度从开发视角审视功能上的实现，而忽略了运维角度的效率提升，功能往往对实际用处不大，我们需要从实际运维角度出发思考产品的最终形态。
4. 前期小而美，开箱即用，在一些常用的功能上提供尽可能标准的代码框架、提供标准的集成部署方案以及生产环境的最佳实践。

从我个人体会上来说：比如自动化的配置备份，可以用difflib也可以用gitlab来做比较，但开发出来后，运维人员的反馈并不热情，使用的积极性不高，归结以下几点：
1. 谁会没事去平台上选择一个配置文件进行比较？ (一般都是紧急事态才会想起来去比)
2. 比较结果并不能直接转化为自动化任务的入参(比如前一天变更失败，需要立即回退，运维发现还不如自己的diff工具顺手)。
3. 配置比较的结果缺乏运营的手段去分析。



## 初版规划
1. 验证TEXTFSM解析器集成，统一数据模型。需要有一个数据模型验证器，确保解析完的数据，是符合我们纳管需求的。
2. 一个基本的网络设备数据模型，可以理解为小型的cmdb，我们只加入网络设备管理所需的基本字段，
包括设备管理账户纳管。目的是为了后期功能开发对接方便，用户使用时可以根据自身需要，继续扩展字段。
3. 验证配置备份功能对接git(也可能是difflib)




```angular2html
├── application
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── dispatch.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── conf
├── del_migrations.py
├── docker_start.sh
├── logs
│├── error.log
│└── server.log
├── manage.py
├── media
│├── config_files
│├── textfsm_templates
└── tools
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── parser_tmp.py  # textfsm解析验证
    ├── tests.py
    └── views.py

```