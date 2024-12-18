PGDMP  &    *            
    |            store     17.2 (Ubuntu 17.2-1.pgdg22.04+1)     17.2 (Ubuntu 17.2-1.pgdg22.04+1) 9    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    24577    store    DATABASE     q   CREATE DATABASE store WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru_RU.UTF-8';
    DROP DATABASE store;
                     postgres    false            �            1255    32785    update_total_cost()    FUNCTION     �   CREATE FUNCTION public.update_total_cost() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW."Общая сумма стоимости товара" := NEW."Кол-во" * NEW."СтоимостьПродажи";
	RETURN NEW;
END;
$$;
 *   DROP FUNCTION public.update_total_cost();
       public               postgres    false            �            1255    32769 #   логировать_запрос()    FUNCTION     �   CREATE FUNCTION public."логировать_запрос"() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    INSERT INTO "ИсторияЗапросов" ("ТекстЗапроса")
    VALUES (current_query());
    RETURN NEW;
END;
$$;
 <   DROP FUNCTION public."логировать_запрос"();
       public               postgres    false            �            1259    24649    klienty_kodklienta_sequence    SEQUENCE     �   CREATE SEQUENCE public.klienty_kodklienta_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.klienty_kodklienta_sequence;
       public               postgres    false            �            1259    24602    Клиенты    TABLE       CREATE TABLE public."Клиенты" (
    "КодКлиента" integer DEFAULT nextval('public.klienty_kodklienta_sequence'::regclass) NOT NULL,
    "ФИО" character varying(255) NOT NULL,
    "Адрес" character varying(255),
    "Телефон" character varying(255)
);
 $   DROP TABLE public."Клиенты";
       public         heap r       postgres    false    227            �            1259    32777    clients_view    VIEW     y  CREATE VIEW public.clients_view AS
 SELECT concat("left"(("ФИО")::text, 2), '***', "right"(("ФИО")::text, 1)) AS "ФИО",
    concat("left"(("Адрес")::text, 5), '***', "right"(("Адрес")::text, 1)) AS "Адрес",
    concat("left"(("Телефон")::text, 5), '***', "right"(("Телефон")::text, 1)) AS "Телефон"
   FROM public."Клиенты";
    DROP VIEW public.clients_view;
       public       v       postgres    false    220    220    220            �            1259    24643    postavka_kodpostavki_sequence    SEQUENCE     �   CREATE SEQUENCE public.postavka_kodpostavki_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.postavka_kodpostavki_sequence;
       public               postgres    false            �            1259    24641 "   postavshik_kodpostavshika_sequence    SEQUENCE     �   CREATE SEQUENCE public.postavshik_kodpostavshika_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.postavshik_kodpostavshika_sequence;
       public               postgres    false            �            1259    24647 !   sotrudniki_kodsotrudnika_sequence    SEQUENCE     �   CREATE SEQUENCE public.sotrudniki_kodsotrudnika_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.sotrudniki_kodsotrudnika_sequence;
       public               postgres    false            �            1259    24645    tovary_kodtovara_sequence    SEQUENCE     �   CREATE SEQUENCE public.tovary_kodtovara_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.tovary_kodtovara_sequence;
       public               postgres    false            �            1259    24651    zakazy_kodzakaza_sequence    SEQUENCE     �   CREATE SEQUENCE public.zakazy_kodzakaza_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.zakazy_kodzakaza_sequence;
       public               postgres    false            �            1259    24585    Заказы    TABLE     �  CREATE TABLE public."Заказы" (
    "КодЗаказа" integer DEFAULT nextval('public.zakazy_kodzakaza_sequence'::regclass) NOT NULL,
    "КодСотрудника" integer NOT NULL,
    "КодТовара" integer NOT NULL,
    "ДатаРазмещения" timestamp without time zone NOT NULL,
    "ДатаИсполнения" timestamp without time zone NOT NULL,
    "КодКлиента" integer NOT NULL
);
 "   DROP TABLE public."Заказы";
       public         heap r       postgres    false    228            �            1259    24654    ИсторияЗапросов    TABLE     �   CREATE TABLE public."ИсторияЗапросов" (
    "КодЗапроса" integer NOT NULL,
    "ТекстЗапроса" text NOT NULL,
    "ВремяЗапроса" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 4   DROP TABLE public."ИсторияЗапросов";
       public         heap r       postgres    false            �            1259    24653 8   История запросов_КодЗапроса_seq    SEQUENCE     �   CREATE SEQUENCE public."История запросов_КодЗапроса_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 Q   DROP SEQUENCE public."История запросов_КодЗапроса_seq";
       public               postgres    false    230            �           0    0 8   История запросов_КодЗапроса_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."История запросов_КодЗапроса_seq" OWNED BY public."ИсторияЗапросов"."КодЗапроса";
          public               postgres    false    229            �            1259    24616    Поставка    TABLE       CREATE TABLE public."Поставка" (
    "КодПоставки" integer DEFAULT nextval('public.postavka_kodpostavki_sequence'::regclass) NOT NULL,
    "КодПоставщика" integer NOT NULL,
    "ДатаПоставки" timestamp without time zone NOT NULL
);
 &   DROP TABLE public."Поставка";
       public         heap r       postgres    false    224            �            1259    24609    Поставщик    TABLE     �  CREATE TABLE public."Поставщик" (
    "КодПоставщика" integer DEFAULT nextval('public.postavshik_kodpostavshika_sequence'::regclass) NOT NULL,
    "НазваниеПоставщика" character varying(255) NOT NULL,
    "ПредставительПоставщика" character varying(255),
    "Обращаться" character varying(255),
    "КонтактныйТелефон" character varying(255),
    "Адрес" character varying(255)
);
 (   DROP TABLE public."Поставщик";
       public         heap r       postgres    false    223            �            1259    24578    Сотрудники    TABLE     #  CREATE TABLE public."Сотрудники" (
    "КодСотрудника" integer DEFAULT nextval('public.sotrudniki_kodsotrudnika_sequence'::regclass) NOT NULL,
    "Фамилия" character varying(255) NOT NULL,
    "Имя" character varying(255) NOT NULL,
    "Отчество" character varying(255) NOT NULL,
    "Должность" character varying(255) NOT NULL,
    "Адрес" character varying(255) NOT NULL,
    "ДомашнийТелефон" character varying(20) NOT NULL,
    "ДатаРождения" date NOT NULL
);
 *   DROP TABLE public."Сотрудники";
       public         heap r       postgres    false    226            �            1259    24595    Товары    TABLE     �  CREATE TABLE public."Товары" (
    "КодТовара" integer DEFAULT nextval('public.tovary_kodtovara_sequence'::regclass) NOT NULL,
    "КодПоставки" integer,
    "НаименованиеТовара" character varying(255) NOT NULL,
    "ТехническиеХарактеристики" character varying(255),
    "Описание" character varying(255),
    "Изображение" bytea,
    "СтоимостьЗакупки" integer,
    "Наличие" boolean,
    "Кол-во" integer,
    "СтоимостьПродажи" integer,
    "Общая сумма стоимости товара" integer
);
 "   DROP TABLE public."Товары";
       public         heap r       postgres    false    225            �           2604    24657 3   ИсторияЗапросов КодЗапроса    DEFAULT     �   ALTER TABLE ONLY public."ИсторияЗапросов" ALTER COLUMN "КодЗапроса" SET DEFAULT nextval('public."История запросов_КодЗапроса_seq"'::regclass);
 f   ALTER TABLE public."ИсторияЗапросов" ALTER COLUMN "КодЗапроса" DROP DEFAULT;
       public               postgres    false    230    229    230            w          0    24585    Заказы 
   TABLE DATA           �   COPY public."Заказы" ("КодЗаказа", "КодСотрудника", "КодТовара", "ДатаРазмещения", "ДатаИсполнения", "КодКлиента") FROM stdin;
    public               postgres    false    218   �V       �          0    24654    ИсторияЗапросов 
   TABLE DATA           �   COPY public."ИсторияЗапросов" ("КодЗапроса", "ТекстЗапроса", "ВремяЗапроса") FROM stdin;
    public               postgres    false    230   'W       y          0    24602    Клиенты 
   TABLE DATA           l   COPY public."Клиенты" ("КодКлиента", "ФИО", "Адрес", "Телефон") FROM stdin;
    public               postgres    false    220   DW       {          0    24616    Поставка 
   TABLE DATA           �   COPY public."Поставка" ("КодПоставки", "КодПоставщика", "ДатаПоставки") FROM stdin;
    public               postgres    false    222   Y       z          0    24609    Поставщик 
   TABLE DATA           �   COPY public."Поставщик" ("КодПоставщика", "НазваниеПоставщика", "ПредставительПоставщика", "Обращаться", "КонтактныйТелефон", "Адрес") FROM stdin;
    public               postgres    false    221   �Y       v          0    24578    Сотрудники 
   TABLE DATA           �   COPY public."Сотрудники" ("КодСотрудника", "Фамилия", "Имя", "Отчество", "Должность", "Адрес", "ДомашнийТелефон", "ДатаРождения") FROM stdin;
    public               postgres    false    217   �[       x          0    24595    Товары 
   TABLE DATA           �  COPY public."Товары" ("КодТовара", "КодПоставки", "НаименованиеТовара", "ТехническиеХарактеристики", "Описание", "Изображение", "СтоимостьЗакупки", "Наличие", "Кол-во", "СтоимостьПродажи", "Общая сумма стоимости товара") FROM stdin;
    public               postgres    false    219   �^       �           0    0    klienty_kodklienta_sequence    SEQUENCE SET     J   SELECT pg_catalog.setval('public.klienty_kodklienta_sequence', 10, true);
          public               postgres    false    227            �           0    0    postavka_kodpostavki_sequence    SEQUENCE SET     L   SELECT pg_catalog.setval('public.postavka_kodpostavki_sequence', 10, true);
          public               postgres    false    224            �           0    0 "   postavshik_kodpostavshika_sequence    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.postavshik_kodpostavshika_sequence', 10, true);
          public               postgres    false    223            �           0    0 !   sotrudniki_kodsotrudnika_sequence    SEQUENCE SET     P   SELECT pg_catalog.setval('public.sotrudniki_kodsotrudnika_sequence', 10, true);
          public               postgres    false    226            �           0    0    tovary_kodtovara_sequence    SEQUENCE SET     H   SELECT pg_catalog.setval('public.tovary_kodtovara_sequence', 11, true);
          public               postgres    false    225            �           0    0    zakazy_kodzakaza_sequence    SEQUENCE SET     H   SELECT pg_catalog.setval('public.zakazy_kodzakaza_sequence', 10, true);
          public               postgres    false    228            �           0    0 8   История запросов_КодЗапроса_seq    SEQUENCE SET     k   SELECT pg_catalog.setval('public."История запросов_КодЗапроса_seq"', 2208, true);
          public               postgres    false    229            �           2606    24589    Заказы Заказы_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public."Заказы"
    ADD CONSTRAINT "Заказы_pkey" PRIMARY KEY ("КодЗаказа");
 L   ALTER TABLE ONLY public."Заказы" DROP CONSTRAINT "Заказы_pkey";
       public                 postgres    false    218            �           2606    24662 C   ИсторияЗапросов История запросов_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."ИсторияЗапросов"
    ADD CONSTRAINT "История запросов_pkey" PRIMARY KEY ("КодЗапроса");
 q   ALTER TABLE ONLY public."ИсторияЗапросов" DROP CONSTRAINT "История запросов_pkey";
       public                 postgres    false    230            �           2606    24608 "   Клиенты Клиенты_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public."Клиенты"
    ADD CONSTRAINT "Клиенты_pkey" PRIMARY KEY ("КодКлиента");
 P   ALTER TABLE ONLY public."Клиенты" DROP CONSTRAINT "Клиенты_pkey";
       public                 postgres    false    220            �           2606    24620 &   Поставка Поставка_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public."Поставка"
    ADD CONSTRAINT "Поставка_pkey" PRIMARY KEY ("КодПоставки");
 T   ALTER TABLE ONLY public."Поставка" DROP CONSTRAINT "Поставка_pkey";
       public                 postgres    false    222            �           2606    24615 *   Поставщик Поставщик_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."Поставщик"
    ADD CONSTRAINT "Поставщик_pkey" PRIMARY KEY ("КодПоставщика");
 X   ALTER TABLE ONLY public."Поставщик" DROP CONSTRAINT "Поставщик_pkey";
       public                 postgres    false    221            �           2606    24584 .   Сотрудники Сотрудники_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."Сотрудники"
    ADD CONSTRAINT "Сотрудники_pkey" PRIMARY KEY ("КодСотрудника");
 \   ALTER TABLE ONLY public."Сотрудники" DROP CONSTRAINT "Сотрудники_pkey";
       public                 postgres    false    217            �           2606    24601    Товары Товары_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public."Товары"
    ADD CONSTRAINT "Товары_pkey" PRIMARY KEY ("КодТовара");
 L   ALTER TABLE ONLY public."Товары" DROP CONSTRAINT "Товары_pkey";
       public                 postgres    false    219            �           1259    32771    clients    INDEX     h   CREATE INDEX clients ON public."Клиенты" USING btree ("ФИО", "Адрес", "Телефон");
    DROP INDEX public.clients;
       public                 postgres    false    220    220    220            �           1259    32775    employee    INDEX     w   CREATE INDEX employee ON public."Сотрудники" USING btree ("Фамилия", "Имя", "Должность");
    DROP INDEX public.employee;
       public                 postgres    false    217    217    217            �           1259    32776    goods    INDEX     �   CREATE INDEX goods ON public."Товары" USING btree ("НаименованиеТовара", "ТехническиеХарактеристики", "Описание");
    DROP INDEX public.goods;
       public                 postgres    false    219    219    219            �           1259    32772    orders    INDEX     �   CREATE INDEX orders ON public."Заказы" USING btree ("КодТовара", "ДатаРазмещения", "ДатаИсполнения");
    DROP INDEX public.orders;
       public                 postgres    false    218    218    218            �           1259    32774    supplier    INDEX     �   CREATE INDEX supplier ON public."Поставщик" USING btree ("НазваниеПоставщика", "ПредставительПоставщика", "Обращаться");
    DROP INDEX public.supplier;
       public                 postgres    false    221    221    221            �           1259    32773    supply    INDEX     �   CREATE INDEX supply ON public."Поставка" USING btree ("КодПоставки", "КодПоставщика", "ДатаПоставки");
    DROP INDEX public.supply;
       public                 postgres    false    222    222    222            �           2620    32786    Товары total_cost    TRIGGER     �   CREATE TRIGGER total_cost BEFORE UPDATE OF "Кол-во" ON public."Товары" FOR EACH ROW WHEN ((new."Кол-во" IS DISTINCT FROM old."Кол-во")) EXECUTE FUNCTION public.update_total_cost();
 2   DROP TRIGGER total_cost ON public."Товары";
       public               postgres    false    219    219    219    233            �           2620    32770 D   ИсторияЗапросов триггер_логирования    TRIGGER     �   CREATE TRIGGER "триггер_логирования" AFTER INSERT OR DELETE OR UPDATE ON public."ИсторияЗапросов" FOR EACH ROW EXECUTE FUNCTION public."логировать_запрос"();
 a   DROP TRIGGER "триггер_логирования" ON public."ИсторияЗапросов";
       public               postgres    false    232    230            �           2606    24626    Заказы klienty_zakazy    FK CONSTRAINT     �   ALTER TABLE ONLY public."Заказы"
    ADD CONSTRAINT klienty_zakazy FOREIGN KEY ("КодКлиента") REFERENCES public."Клиенты"("КодКлиента");
 G   ALTER TABLE ONLY public."Заказы" DROP CONSTRAINT klienty_zakazy;
       public               postgres    false    220    3284    218            �           2606    24631    Товары postavka_tovary    FK CONSTRAINT     �   ALTER TABLE ONLY public."Товары"
    ADD CONSTRAINT postavka_tovary FOREIGN KEY ("КодПоставки") REFERENCES public."Поставка"("КодПоставки");
 H   ALTER TABLE ONLY public."Товары" DROP CONSTRAINT postavka_tovary;
       public               postgres    false    3290    222    219            �           2606    24636 $   Поставка postavshik_postavka    FK CONSTRAINT     �   ALTER TABLE ONLY public."Поставка"
    ADD CONSTRAINT postavshik_postavka FOREIGN KEY ("КодПоставщика") REFERENCES public."Поставщик"("КодПоставщика");
 P   ALTER TABLE ONLY public."Поставка" DROP CONSTRAINT postavshik_postavka;
       public               postgres    false    221    222    3287            �           2606    24590    Заказы sotrudniki_zakazy    FK CONSTRAINT     �   ALTER TABLE ONLY public."Заказы"
    ADD CONSTRAINT sotrudniki_zakazy FOREIGN KEY ("КодСотрудника") REFERENCES public."Сотрудники"("КодСотрудника");
 J   ALTER TABLE ONLY public."Заказы" DROP CONSTRAINT sotrudniki_zakazy;
       public               postgres    false    217    3275    218            �           2606    24621    Заказы tovary_zakazy    FK CONSTRAINT     �   ALTER TABLE ONLY public."Заказы"
    ADD CONSTRAINT tovary_zakazy FOREIGN KEY ("КодТовара") REFERENCES public."Товары"("КодТовара");
 F   ALTER TABLE ONLY public."Заказы" DROP CONSTRAINT tovary_zakazy;
       public               postgres    false    219    3281    218            w   �   x�]��� ϸ��@�Xl~�%��![�iflQ��J.rW�?ȝ��ƚ�AM���B7�I_��Z�c���Ź�Ә�LH͹���&��87Xv�F_��
���|�T6���Bu���}7�n<�+qgُ�g0����|݌�@ϟ�^\T�      �      x������ � �      y   �  x�e��N�0���Sd?��?q�S:?l�ZA��f��D�i��
�o�q
�V���s�u
F4О:`�&��<�������D�������v�����^�L�w�N�[%ji�q��R�[F`;��Զ�1 ��������	o�F|�PJh�KF��Ο�b�3z r����
 |S3#˄,#R�JH %���0��M�07	x	T�W���u�-3�J�*�e�DU]p������: ��z��p����=�W����Y�%E���4�^3Z��l�HF�y�!J<��.�Ej�I�	['��a;��tڏ������hZLy
��0��S7����W�_k'dׁߠ<�{>�:��}H���_ ��G�Z���C-���_;ۘ�EVo��)��嗉��6])j�̹���qj�@o�Lo������ش��n�2�?5BW�$眿�G��      {   w   x�5���0C�oz
-�B�-?2K���)��:�
9<�9��x�M�|:���C���8�]��Ǹ�)?�a�r��'���wAgzU�đ��)����Ɣ,��]~Zk_�U*�      z     x�}�ߎ�@Ư;O��N�v�o|vc�Єc��]��W����p��;�Z܍!���9����MM@s��W��-���_rU�ɍ�D��QH�(p�І|?L��E�3����4�(wC̛�֍Qj�&/19
S��3�Ɣ(Zњ-�k
#I;H�B*]V�9��э0��ZG���߅���F4WE}�g�v-����\O#�
8�&��%�^cV���Ƭ nXg,T����0C��ڽ� �����^����b����j��S�[[�������o0aD5�_p��+Q:C�om�V����O\b)�Ļ>K���iS	˵��q��I3iպz��<�2�����`6�ʳ4�����{�&�?����+m��l=�Zy�1�N�
聾{��h�a�5n�Fq�qo`��Gv�''ye�ȴLLt�z"���Nv�T�ǃ3Bzñ���wǹ�yI��k+y��$@�1��z67���ㅯ���7���B�P]����3�&C��`;<�S�<t�3Z�בR�FB^      v   �  x���͎�0���Sd.��?�3S�D��@ ر�6�fҦ}��7�\;vU@,�%���9ǷH���v4R7=�#m���6��>���2L������ꧧ	j����4$�g�H���kKG�}��j���Sji��@�$�*i�R�BI��6If�M\�L�+~p�=�k^dZ�<�a�-��І���ѧ�7q��s�K��L :�}-=S���T-K#U�LV*P��bm�������z�c<�G��Ba����� ���;aX��� S���2WRi��xV�D��G�a��u"4	}�C�~�����ܵƊ�y_-Y��r�a(|�x�:��$�rYhi٩:�
f��"B�m�}�~�����.��[�o!e5S��́���a�08���,��12�Re��'��"S	��\�*'��g٠W.�lL�_�|^�נt��K5]C��Se*`a����9�-s�)\"c�M�:6.z=���q��	n]��xf�7HGq=�F�m�Ы�e��Ρ.�9ܝ��\\��s��M~���������c��H��Z���j ����Q�����m�?L��,D<S�u���Бw�)=�	�&�GeP ��*�9���?;��Kf��������� 9q�Ϭ+:��^]��<��n!gV�2�D.u&.�� �.B=      x   0  x�}�OJ�@���]�$�����p�R=�+��"<(|^!���̃ע30t�f��_�p r�/Y�� �Y�;9�z{,�6��G��E����؝�'r�)@B�GH�a~��{�8�G�GJ�!_���v����!?W>3;�@h�6EQ��t�)�PQL8r�� ]M�״s�mGR;K��&sq����u]5@{�U����*'�����:�V�~+FΔ�7!��{+n����l|�#x�{�����{|?��m�P�C4~���w����wC���	3� ���0���OC~����	��E��5���4���}     