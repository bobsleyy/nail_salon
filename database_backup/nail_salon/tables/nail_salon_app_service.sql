PGDMP  #                    |            38318020_nailsl3lack    13.13    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24588    38318020_nailsl3lack    DATABASE     �   CREATE DATABASE "38318020_nailsl3lack" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'pl_PL.utf8';
 &   DROP DATABASE "38318020_nailsl3lack";
                38318020_nailsl3lack    false            �            1259    24894    nail_salon_app_service    TABLE     �   CREATE TABLE public.nail_salon_app_service (
    id bigint NOT NULL,
    cost numeric(5,2) NOT NULL,
    execution_time integer NOT NULL,
    service_type_id bigint NOT NULL,
    length_type_id bigint NOT NULL
);
 *   DROP TABLE public.nail_salon_app_service;
       public         heap    38318020_nailsl3lack    false            �            1259    24892    nail_salon_app_service_id_seq    SEQUENCE     �   ALTER TABLE public.nail_salon_app_service ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.nail_salon_app_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          38318020_nailsl3lack    false    227            �          0    24894    nail_salon_app_service 
   TABLE DATA           k   COPY public.nail_salon_app_service (id, cost, execution_time, service_type_id, length_type_id) FROM stdin;
    public          38318020_nailsl3lack    false    227   �       �           0    0    nail_salon_app_service_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.nail_salon_app_service_id_seq', 1, false);
          public          38318020_nailsl3lack    false    226            '           2606    24898 2   nail_salon_app_service nail_salon_app_service_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.nail_salon_app_service
    ADD CONSTRAINT nail_salon_app_service_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.nail_salon_app_service DROP CONSTRAINT nail_salon_app_service_pkey;
       public            38318020_nailsl3lack    false    227            (           1259    24977 /   nail_salon_app_service_service_type_id_1e1fdb29    INDEX     }   CREATE INDEX nail_salon_app_service_service_type_id_1e1fdb29 ON public.nail_salon_app_service USING btree (service_type_id);
 C   DROP INDEX public.nail_salon_app_service_service_type_id_1e1fdb29;
       public            38318020_nailsl3lack    false    227            )           1259    24978 '   nail_salon_app_service_type_id_225286c7    INDEX     t   CREATE INDEX nail_salon_app_service_type_id_225286c7 ON public.nail_salon_app_service USING btree (length_type_id);
 ;   DROP INDEX public.nail_salon_app_service_type_id_225286c7;
       public            38318020_nailsl3lack    false    227            *           2606    25043 P   nail_salon_app_service nail_salon_app_servi_length_type_id_c555ebed_fk_nail_salo    FK CONSTRAINT     �   ALTER TABLE ONLY public.nail_salon_app_service
    ADD CONSTRAINT nail_salon_app_servi_length_type_id_c555ebed_fk_nail_salo FOREIGN KEY (length_type_id) REFERENCES public.nail_salon_app_lengthtype(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.nail_salon_app_service DROP CONSTRAINT nail_salon_app_servi_length_type_id_c555ebed_fk_nail_salo;
       public          38318020_nailsl3lack    false    227            +           2606    24935 Q   nail_salon_app_service nail_salon_app_servi_service_type_id_1e1fdb29_fk_nail_salo    FK CONSTRAINT     �   ALTER TABLE ONLY public.nail_salon_app_service
    ADD CONSTRAINT nail_salon_app_servi_service_type_id_1e1fdb29_fk_nail_salo FOREIGN KEY (service_type_id) REFERENCES public.nail_salon_app_servicetype(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.nail_salon_app_service DROP CONSTRAINT nail_salon_app_servi_service_type_id_1e1fdb29_fk_nail_salo;
       public          38318020_nailsl3lack    false    227            �   k   x�M�Q�0C��a�1�]��9�6M���-�20�p�F��D_�;�Ԏkiz!6p~�	�r�Y4;u��pi�-���^��1��s�@r~.�4Ŀ�"�_!a�afʏk     