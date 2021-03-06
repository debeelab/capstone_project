--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    age integer,
    gender character varying(10),
    movies_id integer NOT NULL
);


ALTER TABLE public.actors OWNER TO udacitystudent;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: udacitystudent
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO udacitystudent;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udacitystudent
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: movie; Type: TABLE; Schema: public; Owner: udacitystudent
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying(50),
    release_date timestamp without time zone
);


ALTER TABLE public.movies OWNER TO udacitystudent;

--
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: udacitystudent
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO udacitystudent;

--
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udacitystudent
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: udacitystudent
--

-- CREATE TABLE public.movies (
--     actor_id integer NOT NULL,
--     movie_id integer NOT NULL
-- );


-- ALTER TABLE public.movies OWNER TO postgres;

--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, age, gender, movies_id) FROM stdin;
1   Will Smith  40  male    1
2	Denzel Washington	45	male    1
3	Bill	35	other   2
4	Juno	30	female  3
\.


--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movies (id, title, release_date) FROM stdin;
1	Blood Diamond	2020-05-04 00:00:00
2	Dream Girls	2010-07-01 00:00:00         
3	The Train	2002-09-01 00:00:00         
4	Yes Man	2012-08-01 00:00:00             
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- COPY public.movies (actor_id, movie_id) FROM stdin;
-- \.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 4, true);


--
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movies_id_seq', 4, true);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

-- ALTER TABLE ONLY public.movies
--     ADD CONSTRAINT movies_pkey PRIMARY KEY (actor_id, movie_id);


--
-- Name: movies movies_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

-- ALTER TABLE ONLY public.movies
--     ADD CONSTRAINT actors_id FOREIGN KEY (actors_id) REFERENCES public.actors(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: movies movies_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT movies_id FOREIGN KEY (movies_id) REFERENCES public.movies(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--