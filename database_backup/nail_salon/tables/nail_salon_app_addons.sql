PGDMP  0                    |            38318020_nailsl3lack    13.13    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24588    38318020_nailsl3lack    DATABASE     �   CREATE DATABASE "38318020_nailsl3lack" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'pl_PL.utf8';
 &   DROP DATABASE "38318020_nailsl3lack";
                38318020_nailsl3lack    false            �            1259    24857    nail_salon_app_addons    TABLE     �   CREATE TABLE public.nail_salon_app_addons (
    id bigint NOT NULL,
    name character varying(64) NOT NULL,
    add_time integer NOT NULL
);
 )   DROP TABLE public.nail_salon_app_addons;
       public         heap    38318020_nailsl3lack    false            �            1259    24855    nail_salon_app_addons_id_seq    SEQUENCE     �   ALTER TABLE public.nail_salon_app_addons ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.nail_salon_app_addons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          38318020_nailsl3lack    false    219            �          0    24857    nail_salon_app_addons 
   TABLE DATA           C   COPY public.nail_salon_app_addons (id, name, add_time) FROM stdin;
    public          38318020_nailsl3lack    false    219   �       �           0    0    nail_salon_app_addons_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.nail_salon_app_addons_id_seq', 1, false);
          public          38318020_nailsl3lack    false    218            (           2606    24863 4   nail_salon_app_addons nail_salon_app_addons_name_key 
   CONSTRAINT     o   ALTER TABLE ONLY public.nail_salon_app_addons
    ADD CONSTRAINT nail_salon_app_addons_name_key UNIQUE (name);
 ^   ALTER TABLE ONLY public.nail_salon_app_addons DROP CONSTRAINT nail_salon_app_addons_name_key;
       public            38318020_nailsl3lack    false    219            *           2606    24861 0   nail_salon_app_addons nail_salon_app_addons_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.nail_salon_app_addons
    ADD CONSTRAINT nail_salon_app_addons_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.nail_salon_app_addons DROP CONSTRAINT nail_salon_app_addons_pkey;
       public            38318020_nailsl3lack    false    219            &           1259    24945 (   nail_salon_app_addons_name_277f3fae_like    INDEX     ~   CREATE INDEX nail_salon_app_addons_name_277f3fae_like ON public.nail_salon_app_addons USING btree (name varchar_pattern_ops);
 <   DROP INDEX public.nail_salon_app_addons_name_277f3fae_like;
       public            38318020_nailsl3lack    false    219            �   F   x�3�t*J��4�2��<ڔ
b�p�%f�fe'9Ɯn�9� �Pi~vb	�i��V�����i����� ���     