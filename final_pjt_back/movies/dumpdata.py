import json
# import requests
genre_result = [
  {
    "genre_ids": 28,
    "name": "액션"
  },
  {
    "genre_ids": 12,
    "name": "모험"
  },
  {
    "genre_ids": 16,
    "name": "애니메이션"
  },
  {
    "genre_ids": 35,
    "name": "코미디"
  },
  {
    "genre_ids": 80,
    "name": "범죄"
  },
  {
    "genre_ids": 99,
    "name": "다큐"
  },
  {
    "genre_ids": 18,
    "name": "드라마"
  },
  {
    "genre_ids": 10751,
    "name": "가족"
  },
  {
    "genre_ids": 14,
    "name": "판타지"
  },
  {
    "genre_ids": 36,
    "name": "역사"
  },
  {
    "genre_ids": 27,
    "name": "호러"
  },
  {
    "genre_ids": 10402,
    "name": "음악"
  },
  {
    "genre_ids": 9648,
    "name": "미스터리"
  },
  {
    "genre_ids": 10749,
    "name": "로맨스"
  },
  {
    "genre_ids": 878,
    "name": "공상 과학"
  },
  {
    "genre_ids": 10770,
    "name": "TV 영화"
  },
  {
    "genre_ids": 53,
    "name": "스릴러"
  },
  {
    "genre_ids": 10752,
    "name": "전쟁"
  },
  {
    "genre_ids": 37,
    "name": "서부극"
  }
]

result = [
    {
      "popularity": 1708.692,
      "vote_count": 352,
      "poster_path": "/7D430eqZj8y3oVkLFfsWXGRcpEG.jpg",
      "id": 528085,
      "backdrop_path": "/5UkzNSOK561c2QRy2Zr4AkADzLT.jpg",
      "original_language": "en",
      "original_title": "2067",
      "genre_ids": [
        878,
        53,
        18
      ],
      "title": "2067",
      "vote_average": 4.7,
      "overview": "",
      "release_date": "2020-10-01"
    },
    {
      "popularity": 1401.739,
      "vote_count": 1483,
      "poster_path": "/j8MRnCjuN7kpM8w3B5hM5mrvTaE.jpg",
      "id": 400160,
      "backdrop_path": "/wu1uilmhM4TdluKi2ytfz8gidHf.jpg",
      "original_language": "en",
      "original_title": "The SpongeBob Movie: Sponge on the Run",
      "genre_ids": [
        14,
        16,
        12,
        35,
        10751
      ],
      "title": "스폰지밥 무비: 핑핑이 구출 대작전",
      "vote_average": 8.1,
      "overview": "우리 핑핑이가 어디로 갔을까? 설마, 납치당한 건가? 사랑하는 반려 달팽이를 찾아 떠나는 스폰지밥. 뚱이도 함께 가야지. 비키니 시티를 벗어나 미지의 세계로, 출발이다!",
      "release_date": "2020-08-14"
    },
    {
      "popularity": 1493.272,
      "vote_count": 157,
      "poster_path": "/ugZW8ocsrfgI95pnQ7wrmKDxIe.jpg",
      "id": 724989,
      "backdrop_path": "/86L8wqGMDbwURPni2t7FQ0nDjsH.jpg",
      "original_language": "en",
      "original_title": "Hard Kill",
      "genre_ids": [
        28,
        53
      ],
      "title": "하드 킬",
      "vote_average": 5,
      "overview": "",
      "release_date": "2020-10-23"
    },
    {
      "popularity": 1226.285,
      "vote_count": 753,
      "poster_path": "/betExZlgK0l7CZ9CsCBVcwO1OjL.jpg",
      "id": 531219,
      "backdrop_path": "/8rIoyM6zYXJNjzGseT3MRusMPWl.jpg",
      "original_language": "en",
      "original_title": "Roald Dahl's The Witches",
      "genre_ids": [
        14,
        10751,
        12,
        35,
        27
      ],
      "title": "마녀를 잡아라",
      "vote_average": 6.9,
      "overview": "마녀들로부터 발각되어 생쥐로 변해버린 소년이 과거 마녀전담반이었던 할머니와 함께 마녀들과 맞선다는 내용의 판타지 어드벤처",
      "release_date": "2020-10-26"
    },
    {
      "popularity": 1283.929,
      "id": 524047,
      "vote_count": 576,
      "vote_average": 7.1,
      "title": "그린랜드",
      "release_date": "2020-07-29",
      "original_language": "en",
      "original_title": "Greenland",
      "genre_ids": [
        28,
        53
      ],
      "backdrop_path": "/2Fk3AB8E9dYIBc2ywJkxk8BTyhc.jpg",
      "overview": "혜성의 지구 충돌 속보를 지켜보던 존과 가족들. 미 항공우주국(NASA)의 예측과 달리 해상으로 떨어졌어야 할 파편은 캘리포니아를 비롯해 세계 대도시로 추락해 세계는 순식간에 혼돈에 빠진다. 지구의 3/4을 날려버릴 초대형 혜성 추락까지 남은 시간은 단 48시간. 존과 가족은 지구의 유일한 안전 대피소인 ‘그린란드’의 벙커로 향하는데... 인류의 마지막 카운트다운이 시작된다!",
      "poster_path": "/wLgHczwajb3QV2JBgsqNVjuHoJC.jpg"
    },
    {
      "popularity": 1135.232,
      "vote_count": 225,
      "poster_path": "/hSpm2mMbkd0hLTRWBz0zolnLAyK.jpg",
      "id": 671039,
      "backdrop_path": "/gnf4Cb2rms69QbCnGFJyqwBWsxv.jpg",
      "original_language": "fr",
      "original_title": "Bronx",
      "genre_ids": [
        53,
        28,
        18,
        80
      ],
      "title": "로그 시티",
      "vote_average": 5.9,
      "overview": "부패경찰과 마르세유의 조폭 사이의 문제로 위기의  경찰조직을 보호해야 한다.",
      "release_date": "2020-10-30"
    },
    {
      "popularity": 856.765,
      "vote_count": 161,
      "poster_path": "/elZ6JCzSEvFOq4gNjNeZsnRFsvj.jpg",
      "id": 741067,
      "backdrop_path": "/aO5ILS7qnqtFIprbJ40zla0jhpu.jpg",
      "original_language": "en",
      "original_title": "Welcome to Sudden Death",
      "genre_ids": [
        28,
        53,
        12,
        18
      ],
      "title": "웰컴 투 서든 데쓰",
      "vote_average": 6.4,
      "overview": "",
      "release_date": "2020-09-29"
    },
    {
      "popularity": 830.124,
      "vote_count": 162,
      "poster_path": "/zfdhsR3Y3xw42OHrMpi0oBw0Uk8.jpg",
      "id": 741074,
      "backdrop_path": "/DA7gzvlBoxMNL0XmGgTZOyv67P.jpg",
      "original_language": "en",
      "original_title": "Once Upon a Snowman",
      "genre_ids": [
        16,
        10751,
        35,
        14
      ],
      "title": "원스 어폰 어 스노우맨",
      "vote_average": 6.9,
      "overview": "",
      "release_date": "2020-10-23"
    },
    {
      "popularity": 783.776,
      "vote_count": 2001,
      "poster_path": "/szItf1XDOY6u0ZeaQFPc3bi1SL0.jpg",
      "id": 613504,
      "backdrop_path": "/6hgItrYQEG33y0I7yP2SRl2ei4w.jpg",
      "original_language": "en",
      "original_title": "After We Collided",
      "genre_ids": [
        10749,
        18
      ],
      "title": "애프터: 그 후",
      "vote_average": 7.3,
      "overview": "\"너만의 테사는 더 이상 없어!\"  첫사랑 하딘이 자신과의 연애를 내기에 걸었다는 비밀을 알게 된 '테사'  둘은 헤어지지만 서로의 살결과 숨결을 끊지 못하며 아슬아슬한 썸을 이어간다. 이후 대학 졸업을 앞둔 취준생 테사는 대형 출판사의 인턴십에 합격하고  거친 하딘과는 180도 다른 젠틀한 직장 남사친 '트레버'를 만나게 된다. \"테사의 두 번째 남자를 만났다\" 런던으로 떠나기 전에 테사를 향한 진심을 전하고 싶었던 '하딘' 테사의 용서를 기다리며 과거의 잘못을 하나씩 고쳐나간다.  워크숍 파티에서 취한 테사의 연락에 하딘은 기대 반, 걱정 반 마음으로 결국 테사의 호텔 룸에 찾아가고, 샤워실에서 그녀석 '트레버'와 마주치는데…",
      "release_date": "2020-09-02"
    },
    {
      "popularity": 883.433,
      "vote_count": 2962,
      "poster_path": "/mQbxBKeRuAofS5p2w4mK7DqtS97.jpg",
      "id": 337401,
      "backdrop_path": "/qAKvUu2FSaDlnqznY4VOp5PmjIF.jpg",
      "original_language": "en",
      "original_title": "Mulan",
      "genre_ids": [
        28,
        12,
        18,
        14
      ],
      "title": "뮬란",
      "vote_average": 7.2,
      "overview": "무예에 남다른 재능을 지닌 뮬란은 좋은 집안과 인연을 맺어 가문을 빛내길 바라는 부모님의 뜻에 따라 본연의 모습을 억누르고 성장한다. 어느 날, 북쪽 오랑캐들이 침입하자 황제는 징집령을 내리고 뮬란은 아픈 아버지를 대신해 가족들 몰래 전장에 나가기로 결심한다. 여자라는 게 발각되면 목숨을 잃을 수도 있는 상황 속에서 뮬란은 타고난 용기와 지혜로 역경을 이겨내며 전사로 성장한다. 마침내 잔인무도한 적장 보리 칸과 마녀 시아니앙을 마주하게 된 뮬란. 그녀는 위험에 빠진 동료와 가족을 구하고 진정한 전사로 거듭날 수 있을 것인가?",
      "release_date": "2020-09-04"
    },
    {
      "popularity": 918.762,
      "id": 571384,
      "vote_count": 60,
      "vote_average": 6.7,
      "title": "컴 플레이",
      "release_date": "2020-10-28",
      "original_language": "en",
      "original_title": "Come Play",
      "genre_ids": [
        27
      ],
      "backdrop_path": "/gkvOmVXdukAwpG8LjTaHo2l2cWU.jpg",
      "overview": "",
      "poster_path": "/e98dJUitAoKLwmzjQ0Yxp1VQrnU.jpg"
    },
    {
      "popularity": 800.839,
      "id": 340102,
      "vote_count": 785,
      "vote_average": 6.3,
      "title": "뉴 뮤턴트",
      "release_date": "2020-08-26",
      "original_language": "en",
      "original_title": "The New Mutants",
      "genre_ids": [
        28,
        878,
        27,
        12
      ],
      "backdrop_path": "/eCIvqa3QVCx6H09bdeOS8Al2Sqy.jpg",
      "overview": "십대의 돌연변이 레인과 일리, 샘, 로베르토는 비밀 시설에 수용되어 심리 상태를 감시 받는다. 이들이 사회에는 물론 스스로에게도 위험한 존재라고 생각하는 닥터 레예스는 이들에게 돌연변이 능력을 통제하는 방법을 가르쳐주고자 애쓴다. 어느 날, 대재앙이 덮친 마을에서 혼자 살아남은 대니가 이곳에 들어오며 끔찍한 일들이 벌어지기 시작하고, 자신들의 힘을 두려워하고 다룰 줄 몰랐던 십대 돌연변이들은 믿기지 않는 경험을 하며 자신들의 능력을 각성하기 시작하는데…",
      "poster_path": "/bqZRy3tJjJIrA38FSdqJEufQ2Os.jpg"
    },
    {
      "popularity": 688.796,
      "vote_count": 2674,
      "poster_path": "/riYInlsq2kf1AWoGm80JQW5dLKp.jpg",
      "id": 497582,
      "backdrop_path": "/kMe4TKMDNXTKptQPAdOF0oZHq3V.jpg",
      "original_language": "en",
      "original_title": "Enola Holmes",
      "genre_ids": [
        80,
        18,
        9648
      ],
      "title": "에놀라 홈즈",
      "vote_average": 7.5,
      "overview": "열여섯 생일을 맞은 셜록의 여동생, 에놀라 홈즈. 사라진 엄마를 찾아 런던으로 향한다. 명석한 두뇌의 대명사인 오빠까지 따돌리고, 위험에 빠진 귀족 청년의 미스터리와 엮이는데. 사건을 추적하며, 홈즈 가문답게 예리한 추리력이 폭발한다. 미스터리 가득한 이 모험, 무사히 마칠 수 있을까?",
      "release_date": "2020-09-23"
    },
    {
      "popularity": 654.464,
      "id": 560050,
      "vote_count": 453,
      "vote_average": 7.6,
      "title": "오버 더 문",
      "release_date": "2020-10-16",
      "original_language": "en",
      "original_title": "Over the Moon",
      "genre_ids": [
        16,
        12,
        10751,
        14
      ],
      "backdrop_path": "/htBUhLSS7FfHtydgYxUWjL3J1Q1.jpg",
      "overview": "믿는 사람에게만 펼쳐지는 세상 똑똑하고 호기심 넘치는 소녀 페이 페이, 엄마가 어린 시절 들려준 전설 속 달의 여신 항아 이야기를 늘 마음에 풀고 살아간다. 일찍 하늘나라로 간 엄마를 그리워하며 살아가던 페이 페이는 어느 날 항아의 전설이 지어낸 이야기일 뿐이라는 고모의 말에 울컥해, 항아의 존재를 증명하기 위해 달로 향하는 로켓을 만들기로 결심한다. 수많은 시행착오 끝에 로켓 만들기에 성공한 페이 페이, 예상치 못한 모험을 떠나게 된 소녀는 신기한 생명체로 가득한 기묘한 세계를 발견하게 되는데…",
      "poster_path": "/zG6QJjd5feBZBl7zeKHDDlgL8FY.jpg"
    },
    {
      "popularity": 683.424,
      "vote_count": 789,
      "poster_path": "/4m6w5gXggWfxeCZD81Pxb9B4hx5.jpg",
      "id": 581392,
      "backdrop_path": "/gEjNlhZhyHeto6Fy5wWy5Uk3A9D.jpg",
      "original_language": "ko",
      "original_title": "반도",
      "genre_ids": [
        28,
        27,
        53
      ],
      "title": "반도",
      "vote_average": 7,
      "overview": "전대미문의 재난 이후 4년이 흐른 대한민국은 버려진 땅이 되어버렸다. 사람들은 고립된 섬이 된 반도에 갇혔고 누구의 생사도 확인할 수 없는 상황에서 정석은 피할 수 없는 미션을 받고 한국 땅에 다시 발을 들인다. 정석은 미지의 세계인 그곳에서 예상치 못한 습격을 받고 일촉즉발의 순간 ‘반도’의 생존자들을 만나게 된다.",
      "release_date": "2020-07-15"
    },
    {
      "popularity": 705.57,
      "vote_count": 13,
      "poster_path": "/AnVD7Gn14uOTQhcc5xYZGQ9DRvS.jpg",
      "id": 624779,
      "backdrop_path": "/h5sUE9jqoYrjsFjANJXL0gpZGye.jpg",
      "original_language": "en",
      "original_title": "VFW",
      "genre_ids": [
        28,
        53,
        27
      ],
      "title": "브이에프더블유",
      "vote_average": 5.2,
      "overview": "옛 전우들이 모여 술을 마시고 대화를 나누는 VFW(해외참전용사) 모임이 있던 밤. 어린 소녀 하나가 훔친 마약을 들고 그 모임에 들이닥친다. 그 뒤를 이어 잔인한 폭력배들이 여자 아이를 추적하면서 그 모임은 소녀와 퇴역군인 모두를 위한 생존 오두막으로 바뀐다. 참전용사들은 마약에 찌든 폭력배들의 끊임없는 공격에 총력전을 펼치기 위해 모을 수 있는 무기를 전부 모아 들이고, 결국 전면전이 뒤따른다.",
      "release_date": "2020-10-14"
    },
    {
      "popularity": 657.51,
      "vote_count": 73,
      "poster_path": "/k8Q9ulyRE8fkvZMkAM9LPYMKctb.jpg",
      "id": 618353,
      "backdrop_path": "/kU7ZiyeUwcpTkYj3UcxSqGdZmxY.jpg",
      "original_language": "en",
      "original_title": "Batman: Death in the Family",
      "genre_ids": [
        16,
        28
      ],
      "title": "배트맨: 데스 인 더 패밀리",
      "vote_average": 7.6,
      "overview": "",
      "release_date": "2020-10-13"
    },
    {
      "popularity": 672.209,
      "vote_count": 192,
      "poster_path": "/m9ZDoCzSbQ7SAOz2tcb1rt6bGG2.jpg",
      "id": 694919,
      "backdrop_path": "/pq0JSpwyT2URytdFG0euztQPAyR.jpg",
      "original_language": "en",
      "original_title": "Money Plane",
      "genre_ids": [
        28
      ],
      "title": "플레인 하이스트",
      "vote_average": 5.9,
      "overview": "마지막 게임에서의 거액의 빚을 갚기 위해 ‘다리우스’ 밑에서 일하게 된 전직 도박꾼 ‘잭’은 전세계 극악무도한 범죄자들이 모여 베팅을 벌이는 ‘머니 플레인’에 탑승해 현금 수백만 달러를 탈취하고 가상 화폐 10억 달러를 해킹하는 미션을 성공시켜야 한다. 하지만 다리우스는 잭을 함정에 빠뜨리고 잭은 플랜B를 가동해 되갚아주려 하는데…!",
      "release_date": "2020-09-29"
    },
    {
      "popularity": 687.708,
      "vote_count": 648,
      "poster_path": "/fJ0i5MKbBTKJGYY2uxsiUMdwMc6.jpg",
      "id": 539885,
      "backdrop_path": "/54yOImQgj8i85u9hxxnaIQBRUuo.jpg",
      "original_language": "en",
      "original_title": "Ava",
      "genre_ids": [
        28,
        80,
        18,
        53
      ],
      "title": "에이바",
      "vote_average": 5.6,
      "overview": "타깃 제거 100%, 실패 확률 0%  킬러 ‘에이바’(제시카 차스테인).  프랑스 최대의 사기범을 제거하는 작전에 투입된 그녀는 임무 중 조직의 금기를 깨트린다. 한편, 그 사실을 알게 된 새로운 보스 ‘사이먼’(콜린 파렐)은 그녀를 제거할 것을 명령하게 되는데… 죽거나, 죽이거나 타깃이 된 그녀, 살기 위한 킬링 액션이 시작된다!",
      "release_date": "2020-07-02"
    },
    {
      "popularity": 511.875,
      "vote_count": 79,
      "poster_path": "/m2FNRngyJMyxLatBMJR8pbeG2v.jpg",
      "id": 635302,
      "backdrop_path": "/d1sVANghKKMZNvqjW0V6y1ejvV9.jpg",
      "original_language": "ja",
      "original_title": "劇場版「鬼滅の刃」無限列車編",
      "genre_ids": [
        16,
        28,
        36,
        12,
        14,
        18
      ],
      "title": "극장판 귀멸의 칼날: 무한열차편",
      "vote_average": 6,
      "overview": "혈귀로 변해버린 여동생 ‘네즈코’를 인간으로 되돌릴 단서를 찾아 비밀조직 귀살대에 들어간 ‘탄지로.’ ‘젠이츠’, ‘이노스케’와 새로운 임무 수행을 위해 무한열차에 탑승 후 귀살대 최강 검사 염주 ‘렌고쿠’와 합류한다. 달리는 무한열차에서 승객들이 하나 둘 흔적 없이 사라지자 숨어있는 식인 혈귀의 존재를 직감하는 ‘렌고쿠’. 귀살대 ‘탄지로’ 일행과 최강 검사 염주 ‘렌고쿠’는 어둠 속을 달리는 무한열차에서 모두의 목숨을 구하기 위해 예측불가능한 능력을 가진 혈귀와 목숨을 건 혈전을 시작하는데…",
      "release_date": "2020-10-16"
    },
    {
      "popularity": 567.237,
      "vote_count": 944,
      "poster_path": "/6agKYU5IQFpuDyUYPu39w7UCRrJ.jpg",
      "id": 740985,
      "backdrop_path": "/hbrXbVoE0NuA1ORoSGGYNASagrl.jpg",
      "original_language": "en",
      "original_title": "Borat Subsequent Moviefilm",
      "genre_ids": [
        35
      ],
      "title": "보랏 속편",
      "vote_average": 6.6,
      "overview": "한때 영광스러운 국가였던 카자흐스탄의 이익을 위해 미국 정권에 엄청난 뇌물 전달하기",
      "release_date": "2020-10-23"
    },
    {
      "popularity": 582.791,
      "id": 718444,
      "vote_count": 364,
      "vote_average": 5.8,
      "title": "로그",
      "release_date": "2020-08-20",
      "original_language": "en",
      "original_title": "Rogue",
      "genre_ids": [
        28,
        12,
        18,
        53
      ],
      "backdrop_path": "/x4UkhIQuHIJyeeOTdcbZ3t3gBSa.jpg",
      "overview": "대장 샘이 이끄는 용병팀 로그는 무장 단체 알샤바브에게 납치된 주지사의 딸을 구출하기 위해 남아프리카 공화국으로 파견된다. 가까스로 타깃 구출에 성공하지만 잔혹하고 무자비한 알샤바브의 추격은 계속되고, 치열한 전투 속 생사의 갈림길에 서게 된 로그 팀 앞에 치명적인 미지의 존재가 등장한다.",
      "poster_path": "/Amkk8KY5Vy81RDrVlDDhd2Ay9ho.jpg"
    },
    {
      "popularity": 560.617,
      "id": 660982,
      "vote_count": 157,
      "vote_average": 6.2,
      "title": "아메리칸 파이: 여자의 규칙",
      "release_date": "2020-10-06",
      "original_language": "en",
      "original_title": "American Pie Presents: Girls' Rules",
      "genre_ids": [
        35
      ],
      "backdrop_path": "/75ooojtgiKYm5LcCczbCexioZze.jpg",
      "overview": "",
      "poster_path": "/xqvX5A24dbIWaeYsMTxxKX5qOfz.jpg"
    },
    {
      "popularity": 630.522,
      "vote_count": 103,
      "poster_path": "/5RbyHIVydD3Krmec1LlUV7rRjet.jpg",
      "id": 622855,
      "backdrop_path": "/6C7ZGYeR8QpT3X6C2RFEu6yiSKK.jpg",
      "original_language": "en",
      "original_title": "Jingle Jangle: A Christmas Journey",
      "genre_ids": [
        10751,
        14,
        10402
      ],
      "title": "징글 쟁글: 저니의 크리스마스",
      "vote_average": 7.4,
      "overview": "화려하고 생기 넘치는 코블튼 마을을 배경으로, 전설적인 장난감 제작자 제로니커스 쟁글의 이야기를 보여준다. 상상 속에서나 볼 법한 그의 발명품들은 기발함과 경이로움으로 가득하다. 그런데 쟁글이 신뢰했던 수습생이 그가 가장 아끼는 장난감을 훔쳐 간다. 이제 희망은 쟁글 못지않게 영리하고 창의적인 손녀에게 달려있다. 그리고 오랫동안 잊고 있던 발명품에. 오랜 상처를 치유하고 내면의 마법을 다시 깨울 수 있을까?",
      "release_date": "2020-11-06"
    },
    {
      "popularity": 452.804,
      "vote_count": 532,
      "poster_path": "/kPzcvxBwt7kEISB9O4jJEuBn72t.jpg",
      "id": 677638,
      "backdrop_path": "/pO1SnM5a1fEsYrFaVZW78Wb0zRJ.jpg",
      "original_language": "en",
      "original_title": "We Bare Bears: The Movie",
      "genre_ids": [
        10751,
        16,
        12,
        35
      ],
      "title": "위 베어 베어스: 더 무비",
      "vote_average": 7.7,
      "overview": "그리즐리, 팬더, 아이스 베어가 푸드 트럭을 얼마나 사랑하는지에 대한 바이럴 비디오가 퍼지게 되면서 생긴 사고로 대규모의 정전 사태가 발발한다. 이 사건은 국립 야생 동물 관리국 소속 트라우트 요원의 관심을 끌게 된다. 트라우트는 인간과 같은 생활 방식을 갖고 있는 곰들을 영원히 격리시킴으로써 자연의 질서를 회복하겠다고 선언한다. 정든 집에서 쫓겨 난 곰들은 캐나다에서 피난처를 찾는 과정에서 새로운 친구, 위험한 장애물, 거대한 파티로 가득 찬 여행을 떠난다. 이 위험천만한 여정은 그들이 처음 만나고 형제가 되었던 예전을 돌아보게 하는데...",
      "release_date": "2020-06-30"
    },
    {
      "popularity": 500.427,
      "id": 475430,
      "vote_count": 946,
      "vote_average": 5.8,
      "title": "아르테미스 파울",
      "release_date": "2020-06-12",
      "original_language": "en",
      "original_title": "Artemis Fowl",
      "genre_ids": [
        12,
        14,
        878,
        10751,
        28
      ],
      "backdrop_path": "/o0F8xAt8YuEm5mEZviX5pEFC12y.jpg",
      "overview": "12살 천재 소년 아르테미스 파울은 유서 깊은 범죄 주모자 집안의 후예이다. 사라진 아버지를 찾으려 하던 중 숨어 있던 강력한 요정 종족이 그 실종 사건의 배후일 수 있다는 것을 알게 된다.",
      "poster_path": "/mhDdx7o7hhrxrikq8aqPLLnS9w8.jpg"
    },
    {
      "popularity": 576.295,
      "id": 332340,
      "vote_count": 662,
      "vote_average": 6.6,
      "title": "런던 시계탑 밑에서 사랑을 찾을 확률",
      "release_date": "2015-05-29",
      "original_language": "en",
      "original_title": "Man Up",
      "genre_ids": [
        10749,
        35
      ],
      "backdrop_path": "/mFjJeakcaiw7KZ4qWBsMStyZGXK.jpg",
      "overview": "매번 실패하는 연애에 어느덧 연애지수 제로가 되어버린 ‘낸시’는 부모님 결혼기념일 파티에 가던 중  우연히 만난 ‘잭’에게 묘한 끌림을 느끼게 된다. 낸시는 얼떨결에 잭의 가짜 소개팅녀 행세를 하게 되고, 두 사람은 런던에서 생애 최고의 유쾌한 데이트를 즐긴다.  하지만 행복도 잠시, 낸시 앞에 나타난 옛 친구덕분에 거짓말로 시작된 데이트는 위기를 맞게 되는데...  올겨울, 누구나 꿈꾸는 솔직발랄 런던 로맨스가 온다!",
      "poster_path": "/6ZzGWclamSIvJMs54sr1NYSmWL3.jpg"
    },
    {
      "popularity": 492.781,
      "vote_count": 25,
      "poster_path": "/vSfchsOaP6xFrLsG6hzXgc3woZ2.jpg",
      "id": 634244,
      "backdrop_path": "/cw8A0SprTxr7uSfcH7lwSRRhezJ.jpg",
      "original_language": "en",
      "original_title": "Heavenquest: A Pilgrim's Progress",
      "genre_ids": [
        12,
        14,
        28
      ],
      "title": "헤븐퀘스트",
      "vote_average": 6.5,
      "overview": "아주 먼 옛날 위대한 에오스 제국은 어둠의 세력의 부활로 무너지게 되고 북왕국과 남왕국의 천 년 전쟁으로 대혼란에 처한다. 왕의 재판관 '반젤'과 그의 친구들, 여전사 '에즈라', 마법사 '엘더'로 구성된 다섯 명의 선택받은 자들은 평화를 지키기 위해 고대 기록의 예언에 따라 빛과 어둠이 존재하는 타락한 관문을 향해 목숨을 건 여정을 떠난다. 한편, 점점 세력을 키워온 어둠의 세력 '아몬'과의 피할 수 없는 전쟁을 앞둔 다섯 명의 선택받은 자들은 드디어 최후의 전쟁을 시작하는데...",
      "release_date": "2020-07-13"
    },
    {
      "popularity": 567.92,
      "vote_count": 57,
      "poster_path": "/2EjUq3eqvDKU4EXh482IQcttcx4.jpg",
      "id": 575088,
      "backdrop_path": "/4br4B8C0SRIYcKHUgoaOlGo50MU.jpg",
      "original_language": "ru",
      "original_title": "Яга. Кошмар тёмного леса",
      "genre_ids": [
        27
      ],
      "title": "바바 야가",
      "vote_average": 6.5,
      "overview": "젊은 가족이 시 외곽의 새 아파트로 이사하며 새로 태어난 아기의 보모를 고용한다.  보모가 집에 들어오면서 이상한 일이 벌어지자 아들 이고르가 부모에게 말하지만 부모는 그 말을 믿지 않는다. 어느 날 집에 돌아온 이고르는 보모와 아기가 사라지고 부모가 이상한 행동을 하며 아기가 있었다는 사실을 기억 못 한다는 사실을 깨닫는다.  친구와 함께 아기를 찾아 나선 이고르는 보모가 바바 야가로 알려진 고대 슬라브 악령이라는 것을 알게 되는데...",
      "release_date": "2020-02-27"
    },
    {
      "popularity": 462.801,
      "id": 734309,
      "vote_count": 156,
      "vote_average": 5.6,
      "title": "산타나",
      "release_date": "2020-08-28",
      "original_language": "en",
      "original_title": "Santana",
      "genre_ids": [
        28
      ],
      "backdrop_path": "/7fvdg211A2L0mHddvzyArRuRalp.jpg",
      "overview": "오래전 부모를 살해한 원수. 마약 조직 보스의 숨겨진 정체가 드디어 드러난다. 성격은 다르지만 목적은 같은 형제. 범죄수사국 요원과 장군이 목숨 건 복수를 시작한다.",
      "poster_path": "/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg"
    },
    {
      "popularity": 420.882,
      "id": 697064,
      "vote_count": 25,
      "vote_average": 5.7,
      "title": "어쌔신 프리스트 벡맨",
      "release_date": "2020-09-10",
      "original_language": "en",
      "original_title": "Beckman",
      "genre_ids": [
        28
      ],
      "backdrop_path": "/7WKIOXJa2JjHygE8Yta3uaCv6GC.jpg",
      "overview": "존경 받는 신부 벡맨은 암살자였던 과거를 숨기고 사이비 교단에서 탈출한 타비타를 입양하여 건실하게 살고 있다. 어느날 사이비 교단의 습격으로 타비타는 납치되고 벡맨은 부상을 당한다. 분노한 벡맨은 다시 암살조직에 복귀해 총을 잡게 되고 교단이 고용한 킬러들과 목숨을 건 대결을 벌인다.",
      "poster_path": "/vxJFueYtoDMK40ZwmyUPCiNaeVl.jpg"
    },
    {
      "popularity": 474.224,
      "vote_count": 187,
      "poster_path": "/eDnHgozW8vfOaLHzfpHluf1GZCW.jpg",
      "id": 606234,
      "backdrop_path": "/u9YEh2xVAPVTKoaMNlB5tH6pXkm.jpg",
      "original_language": "en",
      "original_title": "Archive",
      "genre_ids": [
        878,
        18,
        14,
        53
      ],
      "title": "아카이브",
      "vote_average": 5.8,
      "overview": "2038년 미래 인공 지능을 인간보다 한 단계 더 발전 시키려는 과학자가 불의의 사고를 당한 아내를 죽음으로 부터 불러오는데...",
      "release_date": "2020-08-13"
    },
    {
      "popularity": 446.021,
      "id": 601844,
      "vote_count": 116,
      "vote_average": 6.4,
      "title": "벡키",
      "release_date": "2020-07-23",
      "original_language": "en",
      "original_title": "Becky",
      "genre_ids": [
        28,
        80,
        18,
        53
      ],
      "backdrop_path": "/qTrpw2ZUvN7ywUu1kieEsvNDrgQ.jpg",
      "overview": "아빠와 다툰 후 자신만의 공간에서 홀로 시간을 보내던 십 대 소녀 '벡키'.  같은 시간, 감옥을 탈출한 범죄자들이 무언가를 찾기 위해 벡키의 집으로 들이닥친다. 평소 벡키가 지니고 다니던 열쇠를 찾아, 벡키의 가족들을 위협하는 범죄자들. 그리고 이 사실을 전혀 모르고 있던 백키는 의문의 총소리를 시작으로 혼란에 휩싸이게 되는데...! \"난 너희들을 다치게 할 거야! 기대해도 좋아!\"",
      "poster_path": "/k8Rp9g6kEmlNbNf6Y4fycDCz3uh.jpg"
    },
    {
      "popularity": 488.424,
      "id": 514207,
      "vote_count": 429,
      "vote_average": 7,
      "title": "인베이젼 2020",
      "release_date": "2020-01-01",
      "original_language": "ru",
      "original_title": "Вторжение",
      "genre_ids": [
        878
      ],
      "backdrop_path": "/sizHX5VbwlBihaathTQHVGk1jdi.jpg",
      "overview": "첫 우주 침공으로부터 3년이 지난 지구. 인류는 상처를 이겨내고 조금씩 평범한 일상으로 돌아가고 있다. 그러나 평화도 잠시, 다시 그들이 모습을 드러냈다. 물이 존재하는 그 어느 곳도 안전하지 않은 상황. 하지만 인류는 반드시 이겨낼 것이다!",
      "poster_path": "/kXDm2b90sekbtX1DSBKPzgmFBJb.jpg"
    },
    {
      "popularity": 423.203,
      "vote_count": 5548,
      "poster_path": "/anhvhTzdjzMLzGV8oTFNssvMTIw.jpg",
      "id": 38700,
      "backdrop_path": "/upUy2QhMZEmtypPW3PdieKLAHxh.jpg",
      "original_language": "en",
      "original_title": "Bad Boys for Life",
      "genre_ids": [
        53,
        28,
        80
      ],
      "title": "나쁜 녀석들: 포에버",
      "vote_average": 7.3,
      "overview": "마이애미 강력반의 베테랑 형사 ‘마이크’(윌 스미스)는 여전히 범죄자를 소탕하는 데 열성적이지만, 그의 파트너 ‘마커스’(마틴 로렌스)는 이제 일선에서 물러나 가족과 함께 시간을 보내고 싶어한다. 마커스의 은퇴를 만류하던 마이크가 정체를 알 수 없는 거대 조직의 위협을 받으며 일생일대의 위험에 빠지게 된다. 가족만큼 중요한 마이크를 위해 마커스가 합류하고, 우리의 ‘나쁜 녀석들’은 신식 무기와 기술을 장착한 루키팀 AMMO와 함께 힘을 합쳐 일생일대 마지막 미션을 수행하게 되는데…",
      "release_date": "2020-01-15"
    },
    {
      "popularity": 463.654,
      "id": 635237,
      "vote_count": 48,
      "vote_average": 6.1,
      "title": "킹 아더 카멜롯의 기사",
      "release_date": "2020-05-28",
      "original_language": "en",
      "original_title": "Arthur & Merlin: Knights of Camelot",
      "genre_ids": [
        28,
        12
      ],
      "backdrop_path": "/sFLgXQGrSWxnjmPOpGKPApWNOUH.jpg",
      "overview": "전쟁에서 승리한 아더 왕은 결투자가 되어 은둔한다. 야욕을 가진 왕자는 귀네비어 왕비와 결혼하여 왕좌를 차지하는 음모를 꾸민다. 아더 왕은 빼앗긴 왕국을 되찾기 위해 원탁의 기사들을 소환해 기사도를 맹세하고 대관식 날에 카멜롯 성을 쳐들어가는데… 전설의 기사들이 귀환한다!",
      "poster_path": "/fD6WrWTL2jzKyFE45jGOIuq5E7g.jpg"
    },
    {
      "popularity": 406.864,
      "vote_count": 232,
      "poster_path": "/t28nWRyiwT2cI0KwXYLPwnNltUV.jpg",
      "id": 438396,
      "backdrop_path": "/qGZe9qTuydxyJYQ60XDtEckzLR8.jpg",
      "original_language": "es",
      "original_title": "Orígenes secretos",
      "genre_ids": [
        18,
        53
      ],
      "title": "히어로는 없다",
      "vote_average": 6.2,
      "overview": "히어로는 무슨. 하지만 범죄가 슈퍼히어로 스토리를 빼다 박았다면? 신참 형사가 사건 해결을 위해 공조 아닌 공조를 시작한다. 퍼즐 조각에 불과한 연쇄 살인. 그 큰 그림을 볼 수 있는 건 코믹스라면 꽉 잡은 만화 가게 주인뿐이니까.",
      "release_date": "2020-08-28"
    },
    {
      "popularity": 414.462,
      "vote_count": 1601,
      "poster_path": "/xDZ0tHXxesM34GGLJxr3CCnwPHU.jpg",
      "id": 605116,
      "backdrop_path": "/qVygtf2vU15L2yKS4Ke44U4oMdD.jpg",
      "original_language": "en",
      "original_title": "Project Power",
      "genre_ids": [
        28,
        80,
        878
      ],
      "title": "프로젝트 파워",
      "vote_average": 6.6,
      "overview": "뉴올리언스에 퍼지기 시작한 의문의 약. 강해지고 싶다면 삼켜라. 5분간 엄청난 초능력이 주어진다. 주의사항은? 약을 먹기 전까진 어떤 초능력이 생길지 모른다는 것. 누군가는 총알도 뚫지 못하는 방탄 피부가 되고, 누군가는 투명 인간이 된다. 그리고 또 누군가는 치명적인 능력을 부여받는다. 하지만 가장 큰 문제는 이 약 때문에 범죄 도시로 변하고 있는 뉴올리언스. 이대로 두고 볼 수 없는 경찰 프랭크는 약의 출처를 뒤쫓는다. 마약상인 10대 소녀와 복수를 위해 비밀리에 움직이는 전직 군인과 함께. 이제 어떤 위험을 감수하더라도 그들을 막아야 한다. 파워를 삼켜서라도.",
      "release_date": "2020-08-14"
    },
    {
      "popularity": 436.739,
      "id": 531499,
      "vote_count": 184,
      "vote_average": 6,
      "title": "택스 콜렉터",
      "release_date": "2020-08-07",
      "original_language": "en",
      "original_title": "The Tax Collector",
      "genre_ids": [
        28,
        80,
        18
      ],
      "backdrop_path": "/zogWnCSztU8xvabaepQnAwsOtOt.jpg",
      "overview": "LA 지역 갱들을 관리하며 상납금을 수금하는 최고의 파트너 ‘크리퍼’와 ‘데이비드’. 세상 무서울 것 없는 이들 앞에 조직을 통째로 삼키려는 무법자 ‘코네호’가 나타난다. 지독하고 거칠게 살아남은 두 사람은 조직과 모든 것을 지키기 위해 무자비한 피의 전쟁을 시작하는데…",
      "poster_path": "/yhhJPePGHGtJ6LBVKCyfJg5EBnA.jpg"
    },
    {
      "popularity": 445.785,
      "id": 722603,
      "vote_count": 80,
      "vote_average": 5.9,
      "title": "배틀필드 2025",
      "release_date": "2020-07-07",
      "original_language": "en",
      "original_title": "Battlefield 2025",
      "genre_ids": [
        878,
        27,
        28
      ],
      "backdrop_path": "/m7QpUAeI2xTCJyAVl9J9z5dBTSb.jpg",
      "overview": "",
      "poster_path": "/w6e0XZreiyW4mGlLRHEG8ipff7b.jpg"
    },
    {
      "popularity": 346.747,
      "vote_count": 142,
      "poster_path": "/n6hptKS7Y0ZjkYwbqKOK3jz9XAC.jpg",
      "id": 594328,
      "backdrop_path": "/lkeBhXGJFRlhI7cBWn8LQQAdZqK.jpg",
      "original_language": "en",
      "original_title": "Phineas and Ferb The Movie: Candace Against the Universe",
      "genre_ids": [
        16,
        878,
        35,
        10402,
        10751,
        12
      ],
      "title": "피니와 퍼브: 캔디스 대 우주",
      "vote_average": 7.4,
      "overview": "",
      "release_date": "2020-08-28"
    },
    {
      "popularity": 430.827,
      "vote_count": 37,
      "poster_path": "/4rjHhj1BAREc9zNFU8FheLJQdFf.jpg",
      "id": 621151,
      "backdrop_path": "/5gllGAa3c9UqeRI8r6GXiQJIEtp.jpg",
      "original_language": "en",
      "original_title": "Spell",
      "genre_ids": [
        53,
        27
      ],
      "title": "스펠",
      "vote_average": 5.5,
      "overview": "",
      "release_date": "2020-10-30"
    },
    {
      "popularity": 378.397,
      "vote_count": 1304,
      "poster_path": "/q9KF4CXgK6imiN0Obvg8D7IDRVz.jpg",
      "id": 446893,
      "backdrop_path": "/qsxhnirlp7y4Ae9bd11oYJSX59j.jpg",
      "original_language": "en",
      "original_title": "Trolls World Tour",
      "genre_ids": [
        16,
        10751,
        35,
        14,
        12,
        10402
      ],
      "title": "트롤: 월드 투어",
      "vote_average": 7.5,
      "overview": "노래와 춤을 즐기며 평화로운 나날을 보내던 팝 트롤 파피(안나 켄드릭)와 브랜치(저스틴 팀버레이크) 그리고 친구들. 어느 날 파피는 자신들 외에도 서로 다른 외모와 노래를 가진 5개의 트롤 마을이 더 있다는 것을 알게 된다. 모두와 친구가 되어 신나게 지내고 싶은 파피와 달리 록 트롤 마을의 여왕 바브(레이첼 블룸)는 다른 트롤 마을들을 위협해오고 있다. 바브는 트롤 조상들이 만든 팝, 테크노, 클래식, 컨트리, 펑크, 록 여섯개의 현을 찾아 모든 음악을 통합해, 록을 제외한 음악들을 파괴하려는 위험한 계획을 세운 것. 이를 모르는 팝 트롤들은 다른 음악을 사랑하는 트롤들과도 친구가 될 수 있으리라 믿으며 그들과 어울리기 위한 여행을 떠나는데...",
      "release_date": "2020-03-12"
    },
    {
      "popularity": 373.379,
      "id": 721656,
      "vote_count": 79,
      "vote_average": 7.9,
      "title": "해피 할로윈, 스쿠비 두!",
      "release_date": "2020-10-06",
      "original_language": "en",
      "original_title": "Happy Halloween, Scooby-Doo!",
      "genre_ids": [
        16,
        10751,
        9648,
        35,
        80
      ],
      "backdrop_path": "/5gTQmnGYKxDfmUWJ9GUWqrszRxN.jpg",
      "overview": "",
      "poster_path": "/5aL71e0XBgHZ6zdWcWeuEhwD2Gw.jpg"
    },
    {
      "popularity": 380.648,
      "vote_count": 6340,
      "poster_path": "/sshtRdR9B31LAQbYjwljXGaJ9Kz.jpg",
      "id": 495764,
      "backdrop_path": "/9xNOiv6DZZjH7ABoUUDP0ZynouU.jpg",
      "original_language": "en",
      "original_title": "Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)",
      "genre_ids": [
        28,
        80,
        35
      ],
      "title": "버즈 오브 프레이: 할리 퀸의 황홀한 해방",
      "vote_average": 7.2,
      "overview": "오랜 연인이던 조커와 헤어진 할리 퀸은 처음 맞이한 해방에 황홀함을 느낀다. 하지만 조커라는 방패막이 사라지자 평생 처음 무방비 상태에 놓인 할리 퀸을 고담시에서 가장 비열한 범죄왕 로만 시오니스와 고담의 모든 갱들이 노린다. 통제 불능의 상태에서 카산드라라는 소매치기가 로만의 부하에게서 모든 권력과 고담시 지하 세계 전체의 지배권을 차지할 열쇠인 금융 정보가 암호화되어 있는 다이아몬드를 훔치면서 사건을 걷잡을 수 없이 급변한다. 로만 손에 죽을 위기에 처한 할리 퀸은 헌트리스, 블랙 카나리, 르네 몬토야와 새로운 팀을 결성해 로만에 맞서는데...",
      "release_date": "2020-02-05"
    },
    {
      "popularity": 362.181,
      "id": 330457,
      "vote_count": 6473,
      "vote_average": 7.3,
      "title": "겨울왕국 2",
      "release_date": "2019-11-20",
      "original_language": "en",
      "original_title": "Frozen II",
      "genre_ids": [
        16,
        10751,
        12,
        35,
        14
      ],
      "backdrop_path": "/xJWPZIYOEFIjZpBL7SVBGnzRYXp.jpg",
      "overview": "평화를 되찾은 아렌델 왕국에 새로운 위기가 찾아온다. 어느 날부턴가 의문의 목소리가 엘사를 부르고, 평화로운 아렌델 왕국을 위협한다. 트롤은 모든 것은 과거에서 시작되었음을 알려주며 엘사의 힘의 비밀과 진실을 찾아 떠나야한다고 조언한다. 위험에 빠진 아렌델 왕국을 구해야만 하는 엘사와 안나는 숨겨진 과거의 진실을 찾아 크리스토프, 올라프, 그리고 스벤과 함께 위험천만한 놀라운 모험을 떠나게 된다. 자신의 힘을 두려워했던 엘사는 이제 이 모험을 헤쳐나가기에 자신의 힘이 충분하다고 믿어야만 하는데...",
      "poster_path": "/lVcwSnzhSMWYXUQzyMilCztSE6I.jpg"
    },
    {
      "popularity": 449.998,
      "vote_count": 55,
      "poster_path": "/tBi5xW9Rd0YoGB0aAggV0EN5LDP.jpg",
      "id": 594718,
      "backdrop_path": "/j9uiJPliO5q6xeBO1Buaeqs2qr0.jpg",
      "original_language": "ru",
      "original_title": "Спутник",
      "genre_ids": [
        878,
        18,
        27
      ],
      "title": "스푸트니크",
      "vote_average": 6.4,
      "overview": "1983년 우주궤도를 돌던 소련의 오르비타-4호가 원인불명의 사고로 불시착하고, 생존한 우주비행사 베시냐코프의 이상징후를 진단하기 위해 뇌전문의인 클리모바가 만국과학연구소로 향한다. 그녀는 악화와 회복을 반복하는 베시냐코프를 진찰하면서, 외계의 기생생물이 그의 몸 안으로 침투하여 불시착과 함께 지구로 왔다는 기밀을 알게 된다. 베시냐코프와 기생생물 사이의 공생관계를 파악한 클리모바는 그를 구하기 위해 또 다른 계획을 꾸민다.",
      "release_date": "2020-09-10"
    },
    {
      "popularity": 374.549,
      "vote_count": 18,
      "poster_path": "/frB57nMDmu4NnSzjmrq0lEx5iod.jpg",
      "id": 658412,
      "backdrop_path": "/41OpRg2VZAwzETbwrWtzyF5vACi.jpg",
      "original_language": "hi",
      "original_title": "लूडो",
      "genre_ids": [
        80,
        35
      ],
      "title": "루도 - 인생 게임",
      "vote_average": 7.4,
      "overview": "지우고 싶은 동영상부터 위험천만한 돈 가방까지. 인생을 바꾸려는 네 명의 플레이어가 운명의 게임에 얽혀든다. 판을 좌우하는 건 인생이란 주사위. 당신은 삶을 바꿀 용기가 있는가.",
      "release_date": "2020-11-12"
    },
    {
      "popularity": 386.359,
      "id": 475557,
      "vote_count": 15625,
      "vote_average": 8.2,
      "title": "조커",
      "release_date": "2019-10-02",
      "original_language": "en",
      "original_title": "Joker",
      "genre_ids": [
        80,
        53,
        18
      ],
      "backdrop_path": "/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg",
      "overview": "홀어머니와 사는 아서 플렉은 코미디언을 꿈꾸지만 그의 삶은 좌절과 절망으로 가득 차 있다. 광대 아르바이트는 그에게 모욕을 가져다주기 일쑤고, 긴장하면 웃음을 통제할 수 없는 신경병 증세는 그를 더욱 고립시킨다. 정부 예산 긴축으로 인해 정신과 약물을 지원하던 공공의료 서비스마저 없어져 버린 어느 날, 아서는 지하철에서 시비를 걸어온 증권사 직원들에게 얻어맞던 와중에 동료가 건네준 권총으로 그들을 쏴 버리고 만다. 군중들은 지배계급에 대한 저항의 아이콘이 된 그를 추종하기 시작하며 광대 마스크로 얼굴을 가리고 거리로 쏟아져 나오기 시작하는데...",
      "poster_path": "/wrCwH6WOvXQvVuqcKNUrLDCDxdw.jpg"
    },
    {
      "popularity": 375.02,
      "id": 512895,
      "vote_count": 892,
      "vote_average": 7.3,
      "title": "레이디와 트램프",
      "release_date": "2019-11-12",
      "original_language": "en",
      "original_title": "Lady and the Tramp",
      "genre_ids": [
        10749,
        35,
        10751
      ],
      "backdrop_path": "/73curw674iTzTX81AGaj5dyZUX5.jpg",
      "overview": "부유한 가정에서 살고 있는 레이디(테사 톰슨)는 어느날 개 상인으로부터 자신의 집으로 도망친 트램프(저스틴 서룩스)를 만난다. 처음에는 낯선 그를 경계하지만 이후 안타까운 사연을 듣고 그를 잠시나마 숨겨준다. 그러나 레이디의 주인 부부인 짐 디어(토마스 만),달링(키어시 클레먼스)이 아기 때문에 며칠 동안 집을 배우고 집을 맡기 위해 새로 온 이모 사라(이베트 니콜 브라운)가 데려온 두 고양이로 인해 오해를 받고 집에서 쫓겨난다. 트램프가 위험한 상황에 처한 레이디를 구해준 이후 두 개는 급속도로 가까워진다. 이후 이 사실을 알게 된 부부가 극적으로 레이디를 찾는 데 성공하지만 트램프는 홀로 남게 된다. 여기에 계속해서 끈질기게 트램프를 잡으려는 개 상인의 이들의 뒤를 쫓기 시작한다.",
      "poster_path": "/8wBEye516IKul9sW7JKGcFXVGfV.jpg"
    },
    {
      "popularity": 447.654,
      "id": 682377,
      "vote_count": 9,
      "vote_average": 7.8,
      "title": "치크 파이트",
      "release_date": "2020-11-13",
      "original_language": "en",
      "original_title": "Chick Fight",
      "genre_ids": [
        28,
        35
      ],
      "backdrop_path": "/fTDzKoQIh1HeyjfpG5AHMi2jxAJ.jpg",
      "overview": "",
      "poster_path": "/4ZocdxnOO6q2UbdKye2wgofLFhB.jpg"
    },
    {
      "popularity": 349.265,
      "vote_count": 6124,
      "poster_path": "/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg",
      "id": 454626,
      "backdrop_path": "/stmYfCUGd8Iy6kAMBr6AmWqx8Bq.jpg",
      "original_language": "en",
      "original_title": "Sonic the Hedgehog",
      "genre_ids": [
        28,
        878,
        35,
        10751
      ],
      "title": "수퍼 소닉",
      "vote_average": 7.5,
      "overview": "소리보다 빠른 초고속 고슴도치 히어로 '소닉'은 지구에 불시착한다. 그의 특별한 능력을 감지한 과학자 ‘닥터 로보트닉’은 세계 정복의 야욕을 채우려 하고, 경찰관 ‘톰’은 위험에 빠진 ‘소닉’을 돕기 위해 나서는데…! 과연, ‘소닉'은 천재 악당에 맞서 지구를 지킬 수 있을까?",
      "release_date": "2020-02-12"
    },
    {
      "popularity": 369.622,
      "id": 524216,
      "vote_count": 46,
      "vote_average": 6.5,
      "title": "영안실의 미스테리",
      "release_date": "2020-10-08",
      "original_language": "en",
      "original_title": "The Mortuary Collection",
      "genre_ids": [
        14,
        27
      ],
      "backdrop_path": "/tsGSTBl5H8DBLnHc24Teny0Ppc5.jpg",
      "overview": "샘은 어느 별난 노인이 운영하는 외딴 영안실을 찾아가 자신을 조수로 일하게 해달라고 부탁하는 특이한 젊은 여성이다. 노인과 간단한 인터뷰를 마친 샘은 노인에게 장의사로 영안실에서 일하면서 그가 겪은 가장 무서운 이야기를 해달라고 한다. 노인은 샘에게 1950년대부터 19880년대까지 불길한 비밀을 다룬 네 가지 이야기를 들려준다.",
      "poster_path": "/5WXeYnezavNI6hXH74aQYv6yFzj.jpg"
    },
    {
      "popularity": 327.709,
      "id": 721452,
      "vote_count": 120,
      "vote_average": 7.1,
      "title": "원 나이트 인 방콕",
      "release_date": "2020-08-25",
      "original_language": "en",
      "original_title": "One Night in Bangkok",
      "genre_ids": [
        28,
        53
      ],
      "backdrop_path": "/riDrpqQtZpXGeiJdlmfcwwPH7nN.jpg",
      "overview": "음주 운전자가 낸 교통사고로 죽임을 당하고 억울하게 누명까지 쓴 딸과 가족, 카이는 복수와 정의 실현을 위해 사고를 내고 사건의 조작에 연루된 변호사, 경찰, 도미닉과 그의 부모, 뒷수습을 한 일본인 등 7명을 찾아간다.",
      "poster_path": "/i4kPwXPlM1iy8Jf3S1uuLuwqQAV.jpg"
    },
    {
      "popularity": 319.668,
      "id": 592350,
      "vote_count": 483,
      "vote_average": 8.5,
      "title": "나의 히어로 아카데미아 더 무비: 히어로즈 라이징",
      "release_date": "2019-12-20",
      "original_language": "ja",
      "original_title": "僕のヒーローアカデミア THE MOVIE ヒーローズ：ライジング",
      "genre_ids": [
        16,
        28
      ],
      "backdrop_path": "/9guoVF7zayiiUq5ulKQpt375VIy.jpg",
      "overview": "눈이 계속 내리는 겨울 어느 밤, 히어로 사회를 파괴하려고 계획하는 시가라키 토무라가 인솔하는 빌런 연합과 그 움직임을 사전에 포착한 히어로들의 전투가 전개되는 가운데, 남모르게 조용히 꿈틀거리는 \"뭔가\"가 일어나고, 그 자리를 떠났다. 마침 이즈쿠 일행의 유에이 고교 히어로과 1학년 A반이 은퇴한 No.1 히어로 올마이트의 뒤를 이어 \"차세대 영웅 육성 프로젝트\"의 일환으로 학급 전원에서 기간 한정의 교외 히어로 활동을 위해 일본의 훨씬 남쪽에 위치한 외딴 섬 \"나부 섬\"을 찾았다. 얼마 전 큰 사건이 일어나지 않았던 평화로운 섬에서 이들은 주재 영웅으로서 섬사람들의 생활을 도우며 분주했고, 그러면서도 한가한 시간을 보내고 있었다. 그러나 그 정적을 부수듯이, 갑자기 빌런들이 나부 섬을 덮쳐, 차례차례로 섬의 시설을 파괴해 간다. 그들을 지휘하는 것은, \"나인\". 그날 밤, 눈을 뜬 \"뭔가\"그 자체였다. 이즈쿠와 바쿠고 등의 1학년 A반의 멤버는 힘을 모아 빌런에 맞선다! 과연 섬을 덮치는 나인의 목적이란!? 그리고 이즈쿠 일행의 1학년 A반의 \"뉴 히어로\"들은 이 가장 흉악한 빌런으로부터 섬의 사람들을 지킬 수 있을까!?",
      "poster_path": "/y56HkHAbSZQJjQaxlqCaRI3lIHu.jpg"
    },
    {
      "popularity": 323.841,
      "vote_count": 20196,
      "poster_path": "/kmP6viwzcEkZeoi1LaVcQemcvZh.jpg",
      "id": 299536,
      "backdrop_path": "/lmZFxXgJE3vgrciwuDib0N8CfQo.jpg",
      "original_language": "en",
      "original_title": "Avengers: Infinity War",
      "genre_ids": [
        12,
        28,
        878
      ],
      "title": "어벤져스: 인피니티 워",
      "vote_average": 8.3,
      "overview": "타노스는 6개의 인피니티 스톤을 획득해 신으로 군림하려 한다. 그것은 곧 인류의 절반을 학살해 우주의 균형을 맞추겠다는 뜻. 타노스는 닥터 스트레인지가 소유한 타임 스톤, 비전의 이마에 박혀 있는 마인드 스톤을 차지하기 위해 지구를 침략한다. 아이언맨과 스파이더맨은 가디언즈 오브 갤럭시의 멤버들과 타노스를 상대한다. 지구에선 캡틴 아메리카, 완다, 블랙 위도우, 블랙 팬서 등이 비전을 지키기 위해 뭉친다.",
      "release_date": "2018-04-25"
    },
    {
      "popularity": 333.005,
      "vote_count": 227,
      "poster_path": "/xOmGTJtBgRVSAF4S5dZEUqHqyy5.jpg",
      "id": 621870,
      "backdrop_path": "/oSSEcPDfwgZSv2i01Oqxdb9t8fI.jpg",
      "original_language": "en",
      "original_title": "Secret Society of Second Born Royals",
      "genre_ids": [
        28,
        12,
        35,
        14
      ],
      "title": "시크릿 소사이어티 오브 세컨드 본 로얄",
      "vote_average": 7,
      "overview": "왜? 동화책에는 장남과 장녀, 또는 외동아들과 외동딸 얘기만 있을까? 형, 언니가 왕이 되고 왕비가 되고 콩고물조차 얻어먹지 못해 서러운 둘째 아이들은 동화책에서까지 존재조차 완전히 지워지곤 한다. 왜냐면, 둘째 아이들은 특별한 능력을 지니고 태어나기 때문. 슈퍼히어로 못지 않은 능력으로 동화책 속 왕국을 보호하는 임무를 수행하기 때문에 그들의 존재를 그 누구도 알아서는 안되기 때문이다. 더이상 서럽지 않은 둘째 아이들의 특별한 이야기가 시작된다.",
      "release_date": "2020-09-25"
    },
    {
      "popularity": 286.39,
      "vote_count": 130,
      "poster_path": "/uvD7vPBIpzejysF9e6fQbT5n86O.jpg",
      "id": 611395,
      "backdrop_path": "/qXACJOuyklS0BpvO8ALLkkrsv7W.jpg",
      "original_language": "zh",
      "original_title": "征途",
      "genre_ids": [
        28,
        12,
        14
      ],
      "title": "정도",
      "vote_average": 6.8,
      "overview": "도성의 무술 대회에 부족 대표로 나선 사생아 청년. 어리고 비천하다는 논란이 일지만, 실력으로 가벼이 누르고 출전 자격을 따낸다. 이제 다음 목표는 최종 승자가 되는 것. 그리하여 부족의 명예를 높이고 잃어버린 뿌리도 찾는 것이다.",
      "release_date": "2020-07-21"
    },
    {
      "popularity": 360.417,
      "vote_count": 130,
      "poster_path": "/gEIcPyNduE28kNTMlQ5QN1rbbt7.jpg",
      "id": 425001,
      "backdrop_path": "/a9jZrU7LJk6mAUjmkbEmTiC52l0.jpg",
      "original_language": "en",
      "original_title": "The War with Grandpa",
      "genre_ids": [
        35,
        10751,
        18
      ],
      "title": "워 위드 그랜파",
      "vote_average": 6,
      "overview": "할아버지 ‘에드’에게 방을 뺏겨 다락방 신세가 된 손자 ‘피터’.  방을 되찾기 위해 할아버지를 골탕 먹이려 하지만 호락호락하지 않다. 계속되는 ‘피터’의 도발에 ‘에드’의 반격이 시작되고,  방을 사수하기 위한 소리 없는 전쟁이 시작되는데…!",
      "release_date": "2020-08-27"
    },
    {
      "popularity": 339.444,
      "id": 516486,
      "vote_count": 1369,
      "vote_average": 7.5,
      "title": "그레이하운드",
      "release_date": "2020-07-10",
      "original_language": "en",
      "original_title": "Greyhound",
      "genre_ids": [
        10752,
        28,
        18
      ],
      "backdrop_path": "/xXBnM6uSTk6qqCf0SRZKXcga9Ba.jpg",
      "overview": "1942년 북대서양. 2개월 전 함장이 된 사령관 어니스트 크라우스 중령(톰 행크스)은 처음으로 플레처급 구축함 그레이하운드의 함장으로서 영국으로 향하는 영국으로 향하는 물자를 실은 연합군 수송선단의 호위를 맡게 된다. 출항 전에 애인에게 청혼했지만, 그의 애인은 전시이고 앞으로 어떻게 될지 모르니 아직은 받아들일 수 없다며 고사한다. 선단이 출항하고 얼마 지나지 않아 대잠초계에 나섰던 PBY 카탈리나 수상기가 항속거리 문제로 행운을 빈다면서 돌아간다. 곧이어 기다렸다는 듯이 독일군 U-보트들의 습격이 시작된다. 이틀에 걸쳐 울프팩 전술로 공격하는 네 대의 U-보트를 상대하며 쉴세 없는 추격과 해전이 펼쳐지는데...",
      "poster_path": "/kjMbDciooTbJPofVXgAoFjfX8Of.jpg"
    },
    {
      "popularity": 311.051,
      "vote_count": 3404,
      "poster_path": "/5yaqWb6PnJQuASGTe7c1ontBrUt.jpg",
      "id": 508439,
      "backdrop_path": "/xFxk4vnirOtUxpOEWgA1MCRfy6J.jpg",
      "original_language": "en",
      "original_title": "Onward",
      "genre_ids": [
        16,
        10751,
        12,
        35,
        14
      ],
      "title": "온워드: 단 하루의 기적",
      "vote_average": 7.9,
      "overview": "마법이 사라진 세상, 달라도 너무 다른 두 형제인 용기부족 동생 이안과 의욕충만 형 발리. 이안은 16세 생일날, 엄마에게서 돌아가신 아빠의 선물인 마법봉을 받고 뜻하지 않게 아빠의 반쪽만 소환시키게 되는 상황에 처한다. 아빠의 온전한 모습을 만나기 위해 두 형제에게 주어진 미션. 마법이 통하는 주어진 시간은 단 하루, 두 형제는 모험을 통해 완벽한 아빠의 모습을 만나는 기적을 만들 수 있을까?",
      "release_date": "2020-02-29"
    },
    {
      "popularity": 337.022,
      "vote_count": 113,
      "poster_path": "/bkld8Me0WiLWipLORRNfF1yIPHu.jpg",
      "id": 624963,
      "backdrop_path": "/ezLKohe4HKsHQbwQwhv0ARo83NC.jpg",
      "original_language": "en",
      "original_title": "A Babysitter's Guide to Monster Hunting",
      "genre_ids": [
        12,
        10751,
        14,
        35
      ],
      "title": "베이비시터를 위한 몬스터 사냥 가이드",
      "vote_average": 6.2,
      "overview": "핼러윈에 날벼락을 맞은 10대 소녀. 돌보던 아이가 납치당했다, 그것도 부기맨과 그의 부하 괴물들에게. 그렇다면 싸우는 수밖에. 베이비시터들의 비밀 결사단이 나가신다!",
      "release_date": "2020-10-14"
    },
    {
      "popularity": 308.306,
      "id": 526973,
      "vote_count": 34,
      "vote_average": 6.4,
      "title": "타겟 넘버 원",
      "release_date": "2020-07-10",
      "original_language": "en",
      "original_title": "Target Number One",
      "genre_ids": [
        80,
        53
      ],
      "backdrop_path": "/3DfQYDKKLA8GaTrese7cFDqlSvU.jpg",
      "overview": "헤로인 중독자 다니엘 레저는 잘못된 이유로 잘못된 사람들과의 마약 거래에 관여하게 된다.  거래가 틀어지면서 다니엘은 태국 감옥에 투옥되어 100년형을 선고받는다. 그가 방콕 감옥에서 살아남기 위해 노력하는 동안,  기자 빅터 마라렉은 그의 투옥에 관심을 갖고 다니엘에게 죄를 덮어 씌운 연방 경찰을 추적하기로 결심한다.",
      "poster_path": "/hTQ6CVyA95dYKKbAW8F7srtORDx.jpg"
    },
    {
      "popularity": 301.019,
      "id": 385103,
      "vote_count": 879,
      "vote_average": 7.4,
      "title": "스쿠비!",
      "release_date": "2020-07-08",
      "original_language": "en",
      "original_title": "Scoob!",
      "genre_ids": [
        10751,
        16,
        35,
        12
      ],
      "backdrop_path": "/fKtYXUhX5fxMxzQfyUcQW9Shik6.jpg",
      "overview": "말하는 강아지 스쿠비는 멍뭉이 시절 만난 섀기와 친구들, 그리고 슈퍼히어로 블루 팔콘과 함께 지구에 대재앙을 불러올 무시무시한 음모를 꾸미는 악당 딕에 맞서게 되는데... 스쿠비와 함께 떠나는 미스터리 어드벤쳐! 겁쟁이 스쿠비는 슈퍼 히어로견으로 거듭날 수 있을까?",
      "poster_path": "/mfljcfCzqLU0QIOYiUxmCwEbun1.jpg"
    },
    {
      "popularity": 328.368,
      "id": 547016,
      "vote_count": 2326,
      "vote_average": 7.3,
      "title": "올드 가드",
      "release_date": "2020-07-10",
      "original_language": "en",
      "original_title": "The Old Guard",
      "genre_ids": [
        28,
        14
      ],
      "backdrop_path": "/m0ObOaJBerZ3Unc74l471ar8Iiy.jpg",
      "overview": "수백 년 동안 어둠 속에서 싸워왔다. 인류를 지키는 불멸의 전사들. 큰 잠재력을 가진 신참을 발견하지만, 그들의 놀라운 힘도 발각된다. 잡혀선 안 된다, 끝까지 싸운다.",
      "poster_path": "/65Qf0or6IYVPaxVy7vZXFsHWXAX.jpg"
    },
    {
      "popularity": 312.094,
      "vote_count": 390,
      "poster_path": "/r4Lm1XKP0VsTgHX4LG4syAwYA2I.jpg",
      "id": 590223,
      "backdrop_path": "/lA5fOBqTOQBQ1s9lEYYPmNXoYLi.jpg",
      "original_language": "en",
      "original_title": "Love and Monsters",
      "genre_ids": [
        28,
        12,
        35,
        878
      ],
      "title": "러브 앤 몬스터즈",
      "vote_average": 7.6,
      "overview": "괴물들로 인해 황폐해진 세상. 몬스터포칼립스가 된 세상에서 죽은 줄로만 알았던 여자친구 에이미의 생존 소식을 라디오로 통해 듣고 그녀를 찾아 다시 세상밖으로 나와 한 마디로 사랑 찾아 모험을 떠나는 청년 조엘의 이야기",
      "release_date": "2020-10-16"
    },
    {
      "popularity": 283.668,
      "vote_count": 106,
      "poster_path": "/4BgSWFMW2MJ0dT5metLzsRWO7IJ.jpg",
      "id": 726739,
      "backdrop_path": "/t22fWbzdnThPseipsdpwgdPOPCR.jpg",
      "original_language": "en",
      "original_title": "Cats & Dogs 3: Paws Unite",
      "genre_ids": [
        35,
        28
      ],
      "title": "캣츠 앤 독스 3: 퍼스 유나이트",
      "vote_average": 6.6,
      "overview": "",
      "release_date": "2020-10-02"
    },
    {
      "popularity": 332.012,
      "vote_count": 167,
      "poster_path": "/dnN1ncxEOO1TY0gYL2FWxJqlhlL.jpg",
      "id": 603119,
      "backdrop_path": "/aRyTzHXl9A0vHsd3zd8w2IJxezn.jpg",
      "original_language": "en",
      "original_title": "The Silencing",
      "genre_ids": [
        80,
        53,
        28
      ],
      "title": "사일런싱",
      "vote_average": 6.6,
      "overview": "사냥을 즐기고 술을 좋아하던 레이번 스완슨은 술을 사러 마트에 간 사이에 딸 그웬이 실종된 이후 아내와 이혼하고 애완견 토르와 숲 속 오두막에서 홀로 지낸다. 사냥을 그만두고 자신이 소유한 땅을 딸의 이름을 딴 '그웬 스완슨' 야생동물 보호구역으로 만든 레이번은, 5년이 지난 지금도 딸의 실종 전단을 뿌리며 살아간다.  한편 어릴 적 부모를 잃고 시카고로 홀로 떠난 뒤 동생 브룩스를 위해 다시 고향으로 돌아온 알리스는, 2달 전 에코 폴스의 보안관으로 선출된다.  홀로 남은 브룩스가 헛간에 감금되어 포스터 부부에게 오랫동안 심한 학대를 당했다는 사실을 알게 된 알리스는, 동생을 지켜주지 못한 자신을 용서하지 못한다.  그러던 어느 날, 벅레이크에서 어린 소녀가 창으로 잔인하게 살해되는 사건이 발생하고, 보안관 알리스는 창을 쏘는 '아틀라틀'이라는 무기를 만드는 샘을 찾아간다.  어린 소녀가 누군가에게 쫓기는 장면을 오두막 CCTV를 통해 보게 된 레이번은, 딸 같은 소녀를 구하기 위해 숲 속으로 향하는데...",
      "release_date": "2020-07-18"
    },
    {
      "popularity": 311.331,
      "id": 493065,
      "vote_count": 24,
      "vote_average": 6.2,
      "title": "컷 스로트 시티",
      "release_date": "2020-07-31",
      "original_language": "en",
      "original_title": "Cut Throat City",
      "genre_ids": [
        28,
        80,
        18,
        53
      ],
      "backdrop_path": "/mbvP37gpODCkaCcYkdwK0FFnFKv.jpg",
      "overview": "",
      "poster_path": "/a2Dcje3NkmySevZo5hVCfPaxqdL.jpg"
    },
    {
      "popularity": 264.417,
      "vote_count": 0,
      "poster_path": "/n15reqf2NvUq13mSUOeYftMnBd1.jpg",
      "id": 283566,
      "backdrop_path": "/cdav7lVUviYvQwKB2v73PpaJMFV.jpg",
      "original_language": "ja",
      "original_title": "シン・エヴァンゲリオン劇場版:||",
      "genre_ids": [
        28,
        16,
        18,
        878
      ],
      "title": "신 에반게리온 극장판 :||",
      "vote_average": 0,
      "overview": "",
      "release_date": "2021-01-23"
    },
    {
      "popularity": 290.978,
      "vote_count": 195,
      "poster_path": "/1fUcKFDy58DhWYd5Y7Nu5DgpxaE.jpg",
      "id": 738646,
      "backdrop_path": "/q9ZLjqti3UTt5ZC3qQMZhRNueGc.jpg",
      "original_language": "en",
      "original_title": "Operation Christmas Drop",
      "genre_ids": [
        35,
        10751,
        10749
      ],
      "title": "크리스마스에 날아갑니다",
      "vote_average": 6.8,
      "overview": "망망대해의 열대 섬에 위치한 미국 공군기지. 이곳을 폐쇄할 근거 자료를 수집해야 하는 의원 보좌관. 원리원칙을 따지는 그녀가 기지의 대위에게 흔들린다. 이 남자, 너무 따뜻하잖아?",
      "release_date": "2020-11-05"
    },
    {
      "popularity": 276.832,
      "vote_count": 5317,
      "poster_path": "/kkkS7NYPY4QZcZY6vfkAx0vjJRa.jpg",
      "id": 474350,
      "backdrop_path": "/8moTOzunF7p40oR5XhlDvJckOSW.jpg",
      "original_language": "en",
      "original_title": "It Chapter Two",
      "genre_ids": [
        27,
        14
      ],
      "title": "그것: 두 번째 이야기",
      "vote_average": 6.9,
      "overview": "27년마다 아이들이 사라지는 마을 데리, 또 다시 ‘그것’이 나타났다. 27년 전, 가장 무서워하는 것의 모습으로 나타나 아이들을 잡아먹는 그것 페니와이즈에 맞섰던 ‘루저 클럽’ 친구들은 어른이 되어도 더 커져만 가는 그것의 공포를 끝내기 위해 피할 수 없는 마지막 대결에 나선다.",
      "release_date": "2019-09-04"
    },
    {
      "popularity": 282.897,
      "id": 703134,
      "vote_count": 57,
      "vote_average": 5.5,
      "title": "인퍼머스",
      "release_date": "2020-06-12",
      "original_language": "en",
      "original_title": "Infamous",
      "genre_ids": [
        80,
        53,
        18
      ],
      "backdrop_path": "/j57oUw8LIYvjOl0zs3A1A1UqwKH.jpg",
      "overview": "따분한 동네를 벗어나 유명해지고 싶은 ‘아리엘’은 첫 눈에 반한 ‘딘’과 할리우드로 떠날 계획을 세운다. 어느 날, 우연한 사고로 범죄를 저지르게 된 둘은 인스타그램 라이브를 통해 유명세를 타기 시작하고, 꿈에 다가선 ‘아리엘’과 이 상황을 벗어나고 싶은 딘’은 멈출 수 없는 위험한 질주를 시작한다. 모든 것이 새로워질 거야 11월, Follow me",
      "poster_path": "/lyI5DmqaLjjjpaIsS7WrN4vuvDB.jpg"
    },
    {
      "popularity": 317.409,
      "id": 756278,
      "vote_count": 4,
      "vote_average": 4.5,
      "title": "헌팅 오브 더 메리 셀레스트",
      "release_date": "2020-10-23",
      "original_language": "en",
      "original_title": "Haunting of the Mary Celeste",
      "genre_ids": [
        27
      ],
      "backdrop_path": "/qtq1mai9POAX2IRGcxhVpf8f6Aj.jpg",
      "overview": "",
      "poster_path": "/csTraKglBdSeU9bLMaw9e20hEIN.jpg"
    },
    {
      "popularity": 271.796,
      "vote_count": 741,
      "poster_path": "/lAaJc9842RDVrjvR3OLPMTeHkiA.jpg",
      "id": 615665,
      "backdrop_path": "/dUN960snyYJv3UfCOUEW071Ww7w.jpg",
      "original_language": "en",
      "original_title": "Holidate",
      "genre_ids": [
        35,
        10749
      ],
      "title": "홀리데이트",
      "vote_average": 7.2,
      "overview": "싱글이라 서러운 게 아니다. 또 혼자냐는 잔소리가 지겨울 뿐. 우연히 만난 동병상련 남녀, 명절용 파트너로 계약 체결! 사귀는 척만 하기로 했는데, 자꾸 생각이 난다.",
      "release_date": "2020-10-28"
    },
    {
      "popularity": 284.396,
      "id": 664767,
      "vote_count": 657,
      "vote_average": 8.4,
      "title": "모탈 컴뱃 레전드: 스콜피온의 복수",
      "release_date": "2020-04-12",
      "original_language": "en",
      "original_title": "Mortal Kombat Legends: Scorpion's Revenge",
      "genre_ids": [
        14,
        28,
        12,
        16
      ],
      "backdrop_path": "/9xeEGUZjgiKlI69jwIOi0hjKUIk.jpg",
      "overview": "한 세대에 한 번 꼴로 개최되는 외계와 지구의 챔피언들 간의 토너먼트를 통해 세계의 운명을 결정짓게 되는 이야기. 지구의 수호자인 라이덴 경은 지구에서 가장 강력한 파이터들을 모아 최후의 대결인, 모탈 컴뱃에서 사악한 빌런 상췡으로부터 지구를 지켜야 하는데...",
      "poster_path": "/4VlXER3FImHeFuUjBShFamhIp9M.jpg"
    },
    {
      "popularity": 242.348,
      "id": 324857,
      "vote_count": 8398,
      "vote_average": 8.4,
      "title": "스파이더맨: 뉴 유니버스",
      "release_date": "2018-12-06",
      "original_language": "en",
      "original_title": "Spider-Man: Into the Spider-Verse",
      "genre_ids": [
        28,
        12,
        16,
        878,
        35
      ],
      "backdrop_path": "/aUVCJ0HkcJIBrTJYPnTXta8h9Co.jpg",
      "overview": "평범한 10대 마일스 모랄레스는 우연히 방사능 거미에 물려 스파이더맨 능력을 가지게 된다. 혼란스러워하던 마일스는 악당과 싸우고 있는 피터 파커를 마주치게 되고 피터 파커는 마일스가 자신과 같은 능력을 가지고 있음을 직감한다. 여러 개의 평행세계가 존재한다는 것을 알게 된 마일스와 피터 파커는 이후 스파이더우먼 스파이더 그웬, 스파이더맨 누아르, 스파이더햄 등 평행세계 속 공존하는 모든 스파이더맨들을 만나게 되는데... 하나의 유니버스에서 만나 팀을 결성한 스파이더맨들은 과연 세계를 구할 수 있을까?",
      "poster_path": "/vnWgIIEWAvWKOI65tm6h6VRbyY8.jpg"
    },
    {
      "popularity": 292.058,
      "id": 338762,
      "vote_count": 3327,
      "vote_average": 6.9,
      "title": "블러드샷",
      "release_date": "2020-03-05",
      "original_language": "en",
      "original_title": "Bloodshot",
      "genre_ids": [
        28,
        878
      ],
      "backdrop_path": "/lP5eKh8WOcPysfELrUpGhHJGZEH.jpg",
      "overview": "아내와 함께 휴가를 보내던 특수 부대원 ‘레이’(빈 디젤)는 정체불명의 적에게 납치되어 살해당한다. 혈액 속에 수많은 나노봇을 주입하는 최첨단 프로젝트 블러드샷을 통해 부활한 레이. 놀라운 치유력과 가공할 만한 파워의 슈퍼 히어로로 업그레이드된 레이는 아내를 죽인 놈을 찾아 무차별적인 복수의 질주를 시작한다. 하지만, 자신이 진짜라고 생각했던 것들이 거짓임을 깨닫게 되는데… 복수의 시작, 액션의 끝! 2020년 액션 블록버스터의 최종 진화를 확인하라!",
      "poster_path": "/5S45aZzCo6rIeE8zLsffi5lCYz6.jpg"
    },
    {
      "popularity": 254.511,
      "id": 630566,
      "vote_count": 378,
      "vote_average": 8.5,
      "title": "클라우즈",
      "release_date": "2020-10-09",
      "original_language": "en",
      "original_title": "Clouds",
      "genre_ids": [
        10402,
        18,
        10749
      ],
      "backdrop_path": "/bx326cwBtDsfDcnTgFlK5dXkyaC.jpg",
      "overview": "",
      "poster_path": "/2YvT3pdGngzpbAuxamTz4ZlabnT.jpg"
    },
    {
      "popularity": 263.588,
      "vote_count": 15733,
      "poster_path": "/z7ilT5rNN9kDo8JZmgyhM6ej2xv.jpg",
      "id": 299534,
      "backdrop_path": "/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg",
      "original_language": "en",
      "original_title": "Avengers: Endgame",
      "genre_ids": [
        12,
        878,
        28
      ],
      "title": "어벤져스: 엔드게임",
      "vote_average": 8.3,
      "overview": "어벤져스의 패배 이후 지구는 초토화됐고 남은 절반의 사람들은 정신적 고통을 호소하며 하루하루를 근근이 버텨나간다. 와칸다에서 싸우다 생존한 히어로들과 우주의 타이탄 행성에서 싸우다 생존한 히어로들이 뿔뿔이 흩어졌는데, 아이언맨과 네뷸라는 우주를 떠돌고 있고 지구에 남아 있는 어벤져스 멤버들은 닉 퓨리가 마지막에 신호를 보내다 만 송신기만 들여다보며 혹시 모를 우주의 응답을 기다리는 중이다. 애초 히어로의 삶을 잠시 내려놓고 가족과 시간을 보내던 호크아이 역시 헤아릴 수 없는 마음의 상처를 입은 채 사라지고 마는데...",
      "release_date": "2019-04-24"
    },
    {
      "popularity": 296.836,
      "vote_count": 195,
      "poster_path": "/6zYiIMzIrBidU28QI7cVIJQTkiZ.jpg",
      "id": 489326,
      "backdrop_path": "/dFB6Tiy3z2xRLbnEUB5ocApT5xG.jpg",
      "original_language": "en",
      "original_title": "Mortal",
      "genre_ids": [
        28,
        14,
        53
      ],
      "title": "모탈: 레전드 오브 토르",
      "vote_average": 6.4,
      "overview": "초강력 힘을 가진 '에릭'이 자신을 통제하지 못하고 대혼란을 일으킨다. 경찰서에서 만난 심리학자의 도움으로 자신의 능력을 각성하고 조절하기 시작한다. 한편, 위기를 감지한 미 정보국과 군대가 출동하고 그는 자신의 힘이 북유럽 신화와 연결된 것을 알게 되는데... 선과 악의 경계에 선 천둥의 후계자! 새로운 세계가 열린다!",
      "release_date": "2020-02-28"
    },
    {
      "popularity": 298.334,
      "id": 575774,
      "vote_count": 252,
      "vote_average": 6.5,
      "title": "그 남자의 집",
      "release_date": "2020-01-27",
      "original_language": "en",
      "original_title": "His House",
      "genre_ids": [
        18,
        27,
        53
      ],
      "backdrop_path": "/6aVB2B2GDc4EuNinHgoBgtkuHQz.jpg",
      "overview": "전쟁으로 폐허가 된 남수단에서 한 젊은 부부가 탈출을 감행한다. 생사의 고비를 넘기며 극적으로 도착한 영국. 이곳에서 더 나은 인생을 꿈꾸며 새 보금자리에 입주하지만, 첫날부터 기이한 일들이 일어난다. 쉿, 이 집에 무언가 있다.",
      "poster_path": "/s6XxJEe4ovVTMgmGmKeO87OFANU.jpg"
    },
    {
      "popularity": 301.453,
      "vote_count": 111,
      "poster_path": "/yMr5OI0vX9L8sgf45OTFxp1quLm.jpg",
      "id": 509635,
      "backdrop_path": "/obExOU9qDnMcxvWPumoD14oxup5.jpg",
      "original_language": "en",
      "original_title": "Alone",
      "genre_ids": [
        53
      ],
      "title": "아무도 없다",
      "vote_average": 6.1,
      "overview": "낯선 도로 위에서 사이코패스 살인마의 표적이 된 제시카. 보복 운전과 악질 스토킹 끝에 절대 혼자 빠져나올 수 없는 숲으로 납치된다. 살갗을 찢는 억센 수풀부터 눈을 찌르는 비바람, 누군가 섬뜩하게 지켜보고 있는 듯한 짙은 어둠까지 누구의 도움도 바랄 수 없는 최악의 상황에서 세상 밖으로 탈출하기 위해 살인마와 목숨 건 사투를 벌이는데…",
      "release_date": "2020-09-10"
    },
    {
      "popularity": 279.713,
      "vote_count": 4344,
      "poster_path": "/8MdVJYHKp7JFvTMkLkZOou13LYV.jpg",
      "id": 384018,
      "backdrop_path": "/qAhedRxRYWZAgZ8O8pHIl6QHdD7.jpg",
      "original_language": "en",
      "original_title": "Fast & Furious Presents: Hobbs & Shaw",
      "genre_ids": [
        28,
        12,
        35
      ],
      "title": "분노의 질주: 홉스 & 쇼",
      "vote_average": 6.9,
      "overview": "이상한 약물에 의해 강력한 파워를 얻게 된 아나키스트 브릭스턴 로어(이드리스 엘바)는 인류를 천천히, 그리고 영원히 다른 존재로 바꿔버릴 수 있는 생화학무기를 손에 넣고 자신은 진화형 인간이 된다. 그런데 데카드 쇼(제이슨 스타뎀)의 동생이자 M16 요원인 해티 쇼(바네사 커비)가 치명적인 병원균이 들어 있는 실린더를 브릭스턴의 손에서 훔쳐 달아난다. 양국으로부터 해티의 행방을 찾아달라는 명령을 받은 루크(드웨인 존슨)와 데카드는 유전자 조작으로 사실상 파괴 불가능한 존재가 되어버린 브릭스턴을 상대로 힘겨운 싸움도 이겨나가야 하는데...",
      "release_date": "2019-08-01"
    },
    {
      "popularity": 288.547,
      "vote_count": 5024,
      "poster_path": "/n7KDDIWOY5IZrGlkeizuFMZfJFl.jpg",
      "id": 512200,
      "backdrop_path": "/zTxHf9iIOCqRbxvl8W5QYKrsMLq.jpg",
      "original_language": "en",
      "original_title": "Jumanji: The Next Level",
      "genre_ids": [
        12,
        35,
        14
      ],
      "title": "쥬만지: 넥스트 레벨",
      "vote_average": 7,
      "overview": "쥬만지 게임으로부터 가까스로 탈출해 평화로운 일상을 보내고 있었던 스펜서와 친구들. 어느 날, 스펜서는 망가져버린 쥬만지 게임 속으로 사라지고 그를 찾기 위해 친구들은 다시 위험천만한 게임 속으로 들어간다. 우연히 함께 빨려 들어간 스펜서의 할아버지 에디&마일로와 랜덤으로 선택된 새로운 아바타가 된 이들은 정글부터 설산, 사막까지 한층 진화된 예측 불가능한 게임 속에서 목숨을 건 미션을 수행하게 되는데...",
      "release_date": "2019-12-04"
    },
    {
      "popularity": 281.42,
      "vote_count": 6,
      "poster_path": "/pXv4qbWyj6ycMaWkK2LzlizZQjf.jpg",
      "id": 713825,
      "backdrop_path": "/7r8d5DxzRpC9iq2idNTOa3UyNOw.jpg",
      "original_language": "en",
      "original_title": "Robot Riot",
      "genre_ids": [
        28,
        878
      ],
      "title": "라이어트: 기계들의 역습",
      "vote_average": 5.1,
      "overview": "인공지능이 탑재된 살인 기계에 맞서 기억을 잃은 채 실험에 동원된 군인들이 사투를 벌이는 이야기를 다룬 SF영화",
      "release_date": "2020-06-12"
    },
    {
      "popularity": 251.262,
      "vote_count": 98,
      "poster_path": "/bhNHCeJDFDaB00A46AoCw2mggdE.jpg",
      "id": 601165,
      "backdrop_path": "/nxxODhq9I05Ze9uLONGvfDrzaUO.jpg",
      "original_language": "en",
      "original_title": "Legacy of Lies",
      "genre_ids": [
        53,
        28
      ],
      "title": "레거시 오브 라이즈",
      "vote_average": 5.9,
      "overview": "우크라이나 키예프에서 비밀 임무를 수행하던 영국 MI6 요원 마틴은, 실수로 사랑하는 여인 올가를 총으로 죽이게 된다.  MI6에서 나온 뒤 딸 리스와 함께 영국 런던에서 격투와 술집 보디가드를 하며 생활을 영위하던 마틴은 12년이 지난 지금까지 올가의 환영에 시달린다.  그러던 어느 날, 12년 전 키예프에서의 비밀 임무 중 사망한 우크라이나 기자 스테파넨코의 딸 사샤가, 마틴이 일하는 술집에 나타난다. 사샤는 러시아 화학무기 생산에 대한 정보가 기록된 파일을 찾을 수 있도록 도와달라고 마틴에게 부탁한다.  사샤와 마틴의 만남을 지켜보던 MI6 요원 트레버는 마틴이 파일을 가지고 있다고 의심한다. 그리고  러시아 정보부 요원 티탸나는 마틴의 딸 리사를 인질로 잡고 파일과 함께 사샤를 넘기라고 협박하는데...",
      "release_date": "2020-08-06"
    },
    {
      "popularity": 296.77,
      "vote_count": 174,
      "poster_path": "/v230KtHmd261EA4OSMMSC2TCiA8.jpg",
      "id": 746957,
      "backdrop_path": "/3elhhPDPSD3m0T0SQDJN00O6WhQ.jpg",
      "original_language": "es",
      "original_title": "Ahí te encargo",
      "genre_ids": [
        10749,
        35
      ],
      "title": "아이를 부탁해",
      "vote_average": 8.1,
      "overview": "각자 직장에서 잘나가는 커플. 일도 사랑도 이보다 좋을 순 없다. 딱 하나 문제가 있다면 남편은 아빠가 되고 싶어 죽겠는데, 고속 승진 중인 변호사 아내는 1도 관심 없다는 것. 둘에게 엉뚱한 손님이 찾아오면서, 모든 게 뒤엉킨다!",
      "release_date": "2020-10-02"
    },
    {
      "popularity": 228.265,
      "vote_count": 93,
      "poster_path": "/AwkmMTKJBAatbeAVhTwhcU3Pyp4.jpg",
      "id": 738215,
      "backdrop_path": "/cmZVWuXM1hpP2GKFABCUkoscKu4.jpg",
      "original_language": "en",
      "original_title": "Barbie: Princess Adventure",
      "genre_ids": [
        16,
        10402
      ],
      "title": "바비: 공주의 모험",
      "vote_average": 7.8,
      "overview": "",
      "release_date": "2020-09-01"
    },
    {
      "popularity": 309.145,
      "id": 732670,
      "vote_count": 30,
      "vote_average": 7.5,
      "title": "더 레고 스타 워즈 홀리데이 스페셜",
      "release_date": "2020-11-17",
      "original_language": "en",
      "original_title": "The Lego Star Wars Holiday Special",
      "genre_ids": [
        16,
        12,
        35,
        10751,
        878
      ],
      "backdrop_path": "/1Lhc32P0a62BgMFgd20wXR1osR3.jpg",
      "overview": "",
      "poster_path": "/zyzJSI7UZZzz5Toj10rYGF5689z.jpg"
    },
    {
      "popularity": 226.834,
      "id": 301528,
      "vote_count": 6294,
      "vote_average": 7.6,
      "title": "토이 스토리 4",
      "release_date": "2019-06-19",
      "original_language": "en",
      "original_title": "Toy Story 4",
      "genre_ids": [
        12,
        16,
        35,
        10751,
        14,
        18
      ],
      "backdrop_path": "/q62bpQ67qaXY0u6b2wFEnQYIbPd.jpg",
      "overview": "앤디와 작별한 우디는 새로운 주인 보니와의 생활에 적응 중이다. 보니는 처음 간 유치원에서 불안한 마음을 달래고자 포크를 가지고 새 장난감 포키를 만든다. 쓰레기에서 장난감으로 거듭난 포키는 자꾸 쓰레기통으로 도망치려 하지만 우디는 보니를 위해 포키를 돌봐주기로 한다. 어느 날 가족여행으로 함께 떠난 놀이공원에서 포키가 납치되고, 포키를 구하기 위한 모험을 하던 중 우디는 우연히 오래 전 헤어진 친구 보핍을 만난다. 우디는 주인 없이 자유로운 삶을 살고 있는 보핍을 보며 마음이 흔들리기 시작하는데...",
      "poster_path": "/9P8IX4UyH3QFLL4MV6GZyuOB7Ue.jpg"
    },
    {
      "popularity": 250.758,
      "vote_count": 3261,
      "poster_path": "/rCcL0gv0frDkGLktAbmaAsz7TX6.jpg",
      "id": 545609,
      "backdrop_path": "/1R6cvRtZgsYCkh8UFuWFN33xBP4.jpg",
      "original_language": "en",
      "original_title": "Extraction",
      "genre_ids": [
        18,
        28,
        53
      ],
      "title": "익스트랙션",
      "vote_average": 7.4,
      "overview": "세계에서 가장 위험한 도시로 납치된 의뢰인의 아들을 구하기 위해  전직 특수부대 출신 용병이 거대 범죄 조직에 맞서 벌이는 리얼 액션 구출극.",
      "release_date": "2020-04-24"
    },
    {
      "popularity": 247.816,
      "id": 335983,
      "vote_count": 9855,
      "vote_average": 6.7,
      "title": "베놈",
      "release_date": "2018-09-28",
      "original_language": "en",
      "original_title": "Venom",
      "genre_ids": [
        878,
        28
      ],
      "backdrop_path": "/VuukZLgaCrho2Ar8Scl9HtV3yD.jpg",
      "overview": "진실을 위해서라면 몸을 사리지 않고 사회의 부조리를 취재하는 정의로운 열혈 기자 에디 브록. 거대 기업 라이프 파운데이션의 생체실험에 의혹을 품고 뒤를 쫓던 그는 이들의 사무실에 잠입했다가 실험실에서 외계 생물체 심비오트의 기습 공격을 받게 된다. 심비오트가 숙주의 몸과 정신을 지배할 때 능력을 발휘하는 베놈은 에디의 몸에 기생하며 갖가지 소동을 일으킨다. 한편 비밀리에 인간과 심비오트를 결합해 새로운 생명체를 만들려는 시도를 계속하던 라이프 파운데이션의 회장 드레이크 또한 심비오트의 숙주가 된다.",
      "poster_path": "/lc8TJW5z261JqSz3oSy5GES2ZXj.jpg"
    },
    {
      "popularity": 258.656,
      "id": 360920,
      "vote_count": 2190,
      "vote_average": 6.8,
      "title": "그린치",
      "release_date": "2018-11-08",
      "original_language": "en",
      "original_title": "The Grinch",
      "genre_ids": [
        16,
        10751,
        35,
        14
      ],
      "backdrop_path": "/juc9wt7Eh2IarLL5S1yQ1a21O1A.jpg",
      "overview": "모두가 행복한 크리스마스를 참을 수 없는 그린치는 크리스마스를 훔치기 위해 산타가 되기로 결심한다. 그린치는 만능집사 맥스, 덩치만 큰 소심 루돌프 프레드와 함께 슈퍼배드한 크리스마스 훔치기 대작전에 돌입하는데…",
      "poster_path": "/clJYtRBUhDtvKhPk2HNfXouviKF.jpg"
    },
    {
      "popularity": 245.911,
      "id": 420818,
      "vote_count": 7070,
      "vote_average": 7.2,
      "title": "라이온 킹",
      "release_date": "2019-07-12",
      "original_language": "en",
      "original_title": "The Lion King",
      "genre_ids": [
        12,
        10751,
        10402,
        16
      ],
      "backdrop_path": "/nRXO2SnOA75OsWhNhXstHB8ZmI3.jpg",
      "overview": "혈통을 이어받은 사자가 왕국을 다스리는 아프리카의 프라이드 랜드, 무파사의 아들 심바는 왕좌를 물려받기로 예정되어 있다. 하지만 탐욕스런 무파사의 동생 스카가 자신의 형제를 죽이고, 마치 그 원인이 심바에게 있는 것처럼 분위기를 조장해 그를 왕국에서 쫓아낸다. 아버지의 죽음에 대한 죄책감에 시달리던 심바는 의욕 충만한 친구들 품바와 티몬의 도움으로 희망을 되찾는다. 어느 날 우연히 옛 친구 날라를 만난 심바는 과거를 마주할 용기를 얻고, 진정한 자신의 모습을 찾아 위대하고도 험난한 도전을 떠나게 되는데...",
      "poster_path": "/qlBePshN1ujPwm27JzT6bP6XVeR.jpg"
    },
    {
      "popularity": 231.232,
      "id": 429617,
      "vote_count": 8710,
      "vote_average": 7.5,
      "title": "스파이더맨: 파 프롬 홈",
      "release_date": "2019-06-28",
      "original_language": "en",
      "original_title": "Spider-Man: Far from Home",
      "genre_ids": [
        28,
        12,
        878
      ],
      "backdrop_path": "/5myQbDzw3l8K9yofUXRJ4UTVgam.jpg",
      "overview": "어벤져스 멤버들과 타노스와의 대접전을 마친 뒤, 지난 5년 동안 사라졌던 사람들이 동시에 돌아왔다. 아이언맨이 떠난 채 한동안 지구를 구할 히어로가 공석인 상황을 수습할 히어로는 현재 스파이더맨 피터 파커뿐이다. 친구들과의 유럽 현장학습 도중 닉 퓨리의 부름을 받게 된 피터는 미스테리오라는 정체 모를 히어로와 힘을 합쳐 엘리멘탈이라는 괴생명체를 무찔러야 하는 상황에 처한다. 그런데 피터는 지구를 구하는 일보다 MJ에게 멋지게 고백할 계획이 우선인데...",
      "poster_path": "/v4QlXbktK5smQF49zmclFNntxem.jpg"
    },
    {
      "popularity": 244.232,
      "vote_count": 124,
      "poster_path": "/5pe30v0z4ucVgwh5nR439cCzwwO.jpg",
      "id": 632618,
      "backdrop_path": "/cVdYaAQmd5DZNdo0KFJruz7JpUs.jpg",
      "original_language": "es",
      "original_title": "Crímenes de familia",
      "genre_ids": [
        80,
        18,
        53
      ],
      "title": "가족의 죄",
      "vote_average": 6.5,
      "overview": "전처에 대한 성폭행과 살인미수 혐의로 재판대에 오른 아들. 믿을 수 없는 어머니는 아들의 징역형을 막으려 갖은 애를 쓴다. 하지만 누가 알까. 세상에서 가장 익숙하다고 믿었던 존재에게서 가장 낯선 무엇을 발견하는 순간이 찾아올지도.",
      "release_date": "2020-08-20"
    },
    {
      "popularity": 224.954,
      "vote_count": 17,
      "poster_path": "/cXQQHVTAfn5emTEVm4uqUsE4FIJ.jpg",
      "id": 735110,
      "backdrop_path": "/aahbYclKYfms6Utm5YHQOywsj9N.jpg",
      "original_language": "es",
      "original_title": "Fuego negro",
      "genre_ids": [
        27,
        28,
        53,
        9648
      ],
      "title": "다크 포스",
      "vote_average": 4.6,
      "overview": "",
      "release_date": "2020-08-21"
    },
    {
      "popularity": 217.233,
      "id": 420809,
      "vote_count": 3881,
      "vote_average": 7.4,
      "title": "말레피센트 2",
      "release_date": "2019-10-16",
      "original_language": "en",
      "original_title": "Maleficent: Mistress of Evil",
      "genre_ids": [
        14,
        10751,
        12
      ],
      "backdrop_path": "/skvI4rYFrKXS73BJxWGH54Omlvv.jpg",
      "overview": "무어스 숲의 수호신이자 어둠의 지배자인 말레피센트는 딸처럼 키운 오로라 공주와 필립 왕자의 결혼을 탐탁지 않게 여긴다. 배신당한 과거 때문에 인간을 믿지 못하는 말레피센트는 오찬 자리에서 필립 왕자의 어머니인 잉그리스 왕비와 언쟁을 나누며 신경전을 벌인다. 그 과정에서 누명을 뒤집어쓴 말레피센트는 마음의 상처를 입고 돌아가다 습격을 받고 바닷속으로 추락한다. 요정과 인간의 대립이 전쟁으로 번져나가는 와중에 요정과 인간, 어머니와 딸, 믿음과 불신 사이에서 말레피센트와 오로라는 깊은 고민에 빠지는데...",
      "poster_path": "/btpvGjqLBHgRnobKGlzbBD4jzmf.jpg"
    },
]

dumpdata = []
for genre in genre_result:
  dumpdata.append({
    "model" : "movies.genre",
    "pk": genre.get("genre_ids"),
    "fields": {
      'name': genre.get('name')
    }
  })

for i in range(len(result)):
  dumpdata.append({
    "model":"movies.movie",
    "fields": {
      "title":result[i].get("title"),
      "release_date":result[i].get("release_date"),
      "popularity":result[i].get("popularity"),
      "vote_count":result[i].get("vote_count"),
      "vote_average":result[i].get("vote_average"),
      "overview":result[i].get("overview"),
      "poster_path":f'https://image.tmdb.org/t/p/w500/{result[i].get("poster_path")}',
      "genre_ids":result[i].get("genre_ids"),
    }
  }
  )


with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(dumpdata, ensure_ascii=False))
