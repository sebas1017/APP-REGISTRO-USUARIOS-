PGDMP     6        
            y            Crud    13.1    13.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24784    Crud    DATABASE     e   CREATE DATABASE "Crud" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE "Crud";
                postgres    false            �            1255    24836 
   myinsert()    FUNCTION     �   CREATE FUNCTION public.myinsert() RETURNS boolean
    LANGUAGE plpgsql
    AS $$
      BEGIN
        INSERT INTO foo (bar)
        VALUES('hola');
         return true;
      END;
  $$;
 !   DROP FUNCTION public.myinsert();
       public          postgres    false            �            1259    41309    users    TABLE     �   CREATE TABLE public.users (
    cedula numeric NOT NULL,
    nombre character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    direccion character varying(80) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �          0    41309    users 
   TABLE DATA           A   COPY public.users (cedula, nombre, email, direccion) FROM stdin;
    public          postgres    false    200   �       #           2606    41316    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (cedula);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    200            �   9   x�3152!�ļ���b��Ģ��bcS��������\��DS]cSc�=... �tZ     