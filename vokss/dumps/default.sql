--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.4

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
-- Name: atelier_allowancediscount; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_allowancediscount (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    coefficient numeric(5,2) NOT NULL,
    label character varying(255) NOT NULL
);


ALTER TABLE public.atelier_allowancediscount OWNER TO dbdev;

--
-- Name: atelier_allowancediscount_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_allowancediscount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_allowancediscount_id_seq OWNER TO dbdev;

--
-- Name: atelier_allowancediscount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_allowancediscount_id_seq OWNED BY public.atelier_allowancediscount.id;


--
-- Name: atelier_client; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_client (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    tel_number character varying(30) NOT NULL,
    place character varying(30) NOT NULL
);


ALTER TABLE public.atelier_client OWNER TO dbdev;

--
-- Name: atelier_client_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_client_id_seq OWNER TO dbdev;

--
-- Name: atelier_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_client_id_seq OWNED BY public.atelier_client.id;


--
-- Name: atelier_complicationelement; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_complicationelement (
    id integer NOT NULL,
    name character varying(264) NOT NULL,
    base_price numeric(5,2) NOT NULL,
    complexity numeric(3,2) NOT NULL,
    "group" character varying(255) NOT NULL
);


ALTER TABLE public.atelier_complicationelement OWNER TO dbdev;

--
-- Name: atelier_complicationelement_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_complicationelement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_complicationelement_id_seq OWNER TO dbdev;

--
-- Name: atelier_complicationelement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_complicationelement_id_seq OWNED BY public.atelier_complicationelement.id;


--
-- Name: atelier_fabric; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_fabric (
    id integer NOT NULL,
    name character varying(264) NOT NULL,
    "group" character varying(3) NOT NULL,
    complexity_factor numeric(5,2) NOT NULL
);


ALTER TABLE public.atelier_fabric OWNER TO dbdev;

--
-- Name: atelier_fabric_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_fabric_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_fabric_id_seq OWNER TO dbdev;

--
-- Name: atelier_fabric_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_fabric_id_seq OWNED BY public.atelier_fabric.id;


--
-- Name: atelier_minimalstyle; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_minimalstyle (
    id integer NOT NULL,
    name text NOT NULL,
    "group" character varying(264) NOT NULL
);


ALTER TABLE public.atelier_minimalstyle OWNER TO dbdev;

--
-- Name: atelier_minimalstyle_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_minimalstyle_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_minimalstyle_id_seq OWNER TO dbdev;

--
-- Name: atelier_minimalstyle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_minimalstyle_id_seq OWNED BY public.atelier_minimalstyle.id;


--
-- Name: atelier_order; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_order (
    id integer NOT NULL,
    processing_category character varying(1) NOT NULL,
    order_date date NOT NULL,
    client_id integer NOT NULL,
    fabric_id integer NOT NULL,
    product_id integer NOT NULL
);


ALTER TABLE public.atelier_order OWNER TO dbdev;

--
-- Name: atelier_order_allowance_discount; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_order_allowance_discount (
    id integer NOT NULL,
    order_id integer NOT NULL,
    allowancediscount_id integer NOT NULL
);


ALTER TABLE public.atelier_order_allowance_discount OWNER TO dbdev;

--
-- Name: atelier_order_allowance_discount_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_order_allowance_discount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_order_allowance_discount_id_seq OWNER TO dbdev;

--
-- Name: atelier_order_allowance_discount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_order_allowance_discount_id_seq OWNED BY public.atelier_order_allowance_discount.id;


--
-- Name: atelier_order_complication_elements; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_order_complication_elements (
    id integer NOT NULL,
    order_id integer NOT NULL,
    complicationelement_id integer NOT NULL
);


ALTER TABLE public.atelier_order_complication_elements OWNER TO dbdev;

--
-- Name: atelier_order_complication_elements_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_order_complication_elements_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_order_complication_elements_id_seq OWNER TO dbdev;

--
-- Name: atelier_order_complication_elements_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_order_complication_elements_id_seq OWNED BY public.atelier_order_complication_elements.id;


--
-- Name: atelier_order_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_order_id_seq OWNER TO dbdev;

--
-- Name: atelier_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_order_id_seq OWNED BY public.atelier_order.id;


--
-- Name: atelier_product; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.atelier_product (
    id integer NOT NULL,
    name character varying(264) NOT NULL,
    base_price numeric(10,2) NOT NULL,
    minimal_style_id integer NOT NULL
);


ALTER TABLE public.atelier_product OWNER TO dbdev;

--
-- Name: atelier_product_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.atelier_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atelier_product_id_seq OWNER TO dbdev;

--
-- Name: atelier_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.atelier_product_id_seq OWNED BY public.atelier_product.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO dbdev;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO dbdev;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO dbdev;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO dbdev;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO dbdev;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO dbdev;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO dbdev;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO dbdev;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO dbdev;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO dbdev;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO dbdev;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO dbdev;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO dbdev;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO dbdev;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO dbdev;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO dbdev;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO dbdev;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: dbdev
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO dbdev;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbdev
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: dbdev
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO dbdev;

--
-- Name: atelier_allowancediscount id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_allowancediscount ALTER COLUMN id SET DEFAULT nextval('public.atelier_allowancediscount_id_seq'::regclass);


--
-- Name: atelier_client id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_client ALTER COLUMN id SET DEFAULT nextval('public.atelier_client_id_seq'::regclass);


--
-- Name: atelier_complicationelement id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_complicationelement ALTER COLUMN id SET DEFAULT nextval('public.atelier_complicationelement_id_seq'::regclass);


--
-- Name: atelier_fabric id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_fabric ALTER COLUMN id SET DEFAULT nextval('public.atelier_fabric_id_seq'::regclass);


--
-- Name: atelier_minimalstyle id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_minimalstyle ALTER COLUMN id SET DEFAULT nextval('public.atelier_minimalstyle_id_seq'::regclass);


--
-- Name: atelier_order id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order ALTER COLUMN id SET DEFAULT nextval('public.atelier_order_id_seq'::regclass);


--
-- Name: atelier_order_allowance_discount id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_allowance_discount ALTER COLUMN id SET DEFAULT nextval('public.atelier_order_allowance_discount_id_seq'::regclass);


--
-- Name: atelier_order_complication_elements id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_complication_elements ALTER COLUMN id SET DEFAULT nextval('public.atelier_order_complication_elements_id_seq'::regclass);


--
-- Name: atelier_product id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_product ALTER COLUMN id SET DEFAULT nextval('public.atelier_product_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: atelier_allowancediscount; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_allowancediscount (id, name, coefficient, label) FROM stdin;
\.


--
-- Data for Name: atelier_client; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_client (id, first_name, last_name, tel_number, place) FROM stdin;
\.


--
-- Data for Name: atelier_complicationelement; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_complicationelement (id, name, base_price, complexity, "group") FROM stdin;
\.


--
-- Data for Name: atelier_fabric; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_fabric (id, name, "group", complexity_factor) FROM stdin;
\.


--
-- Data for Name: atelier_minimalstyle; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_minimalstyle (id, name, "group") FROM stdin;
\.


--
-- Data for Name: atelier_order; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_order (id, processing_category, order_date, client_id, fabric_id, product_id) FROM stdin;
\.


--
-- Data for Name: atelier_order_allowance_discount; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_order_allowance_discount (id, order_id, allowancediscount_id) FROM stdin;
\.


--
-- Data for Name: atelier_order_complication_elements; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_order_complication_elements (id, order_id, complicationelement_id) FROM stdin;
\.


--
-- Data for Name: atelier_product; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.atelier_product (id, name, base_price, minimal_style_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add allowance discount	7	add_allowancediscount
26	Can change allowance discount	7	change_allowancediscount
27	Can delete allowance discount	7	delete_allowancediscount
28	Can view allowance discount	7	view_allowancediscount
29	Can add client	8	add_client
30	Can change client	8	change_client
31	Can delete client	8	delete_client
32	Can view client	8	view_client
33	Can add complication element	9	add_complicationelement
34	Can change complication element	9	change_complicationelement
35	Can delete complication element	9	delete_complicationelement
36	Can view complication element	9	view_complicationelement
37	Can add fabric	10	add_fabric
38	Can change fabric	10	change_fabric
39	Can delete fabric	10	delete_fabric
40	Can view fabric	10	view_fabric
41	Can add minimal style	11	add_minimalstyle
42	Can change minimal style	11	change_minimalstyle
43	Can delete minimal style	11	delete_minimalstyle
44	Can view minimal style	11	view_minimalstyle
45	Can add product	12	add_product
46	Can change product	12	change_product
47	Can delete product	12	delete_product
48	Can view product	12	view_product
49	Can add order	13	add_order
50	Can change order	13	change_order
51	Can delete order	13	delete_order
52	Can view order	13	view_order
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$zsgmTd2Yt592$JZeR4QQqjqbXRFguPCsjcORzTDQEeWcDoBcq3+z5K0Q=	2019-09-22 10:09:04.604566+03	t	grandma@example.com			grandma@example.com	t	t	2019-09-22 10:08:56.711791+03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	atelier	allowancediscount
8	atelier	client
9	atelier	complicationelement
10	atelier	fabric
11	atelier	minimalstyle
12	atelier	product
13	atelier	order
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-09-22 10:06:49.123293+03
2	auth	0001_initial	2019-09-22 10:06:49.151318+03
3	admin	0001_initial	2019-09-22 10:06:49.190564+03
4	admin	0002_logentry_remove_auto_add	2019-09-22 10:06:49.20341+03
5	admin	0003_logentry_add_action_flag_choices	2019-09-22 10:06:49.210934+03
6	atelier	0001_initial	2019-09-22 10:06:49.250205+03
7	contenttypes	0002_remove_content_type_name	2019-09-22 10:06:49.287256+03
8	auth	0002_alter_permission_name_max_length	2019-09-22 10:06:49.291917+03
9	auth	0003_alter_user_email_max_length	2019-09-22 10:06:49.29946+03
10	auth	0004_alter_user_username_opts	2019-09-22 10:06:49.307164+03
11	auth	0005_alter_user_last_login_null	2019-09-22 10:06:49.316935+03
12	auth	0006_require_contenttypes_0002	2019-09-22 10:06:49.318448+03
13	auth	0007_alter_validators_add_error_messages	2019-09-22 10:06:49.329118+03
14	auth	0008_alter_user_username_max_length	2019-09-22 10:06:49.341159+03
15	auth	0009_alter_user_last_name_max_length	2019-09-22 10:06:49.350723+03
16	auth	0010_alter_group_name_max_length	2019-09-22 10:06:49.359367+03
17	auth	0011_update_proxy_permissions	2019-09-22 10:06:49.373296+03
18	sessions	0001_initial	2019-09-22 10:06:49.379771+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: dbdev
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
0h06ztvugcsb46kf23uzldl43xyp5xk6	YzAwNWQwNzI4NWYwZDY4MzdmYjdkNjRmNGFjNzE4NTQ4OTI3ODk5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0ZjA0N2I0ZTQwZmFhY2E3YmVjMzAyODkyYjNiMTYyMDAxOWVmNzgwIn0=	2019-10-06 10:09:04.606474+03
\.


--
-- Name: atelier_allowancediscount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_allowancediscount_id_seq', 1, false);


--
-- Name: atelier_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_client_id_seq', 1, false);


--
-- Name: atelier_complicationelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_complicationelement_id_seq', 1, false);


--
-- Name: atelier_fabric_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_fabric_id_seq', 1, false);


--
-- Name: atelier_minimalstyle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_minimalstyle_id_seq', 1, false);


--
-- Name: atelier_order_allowance_discount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_order_allowance_discount_id_seq', 1, false);


--
-- Name: atelier_order_complication_elements_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_order_complication_elements_id_seq', 1, false);


--
-- Name: atelier_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_order_id_seq', 1, false);


--
-- Name: atelier_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.atelier_product_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbdev
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);


--
-- Name: atelier_allowancediscount atelier_allowancediscount_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_allowancediscount
    ADD CONSTRAINT atelier_allowancediscount_pkey PRIMARY KEY (id);


--
-- Name: atelier_client atelier_client_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_client
    ADD CONSTRAINT atelier_client_pkey PRIMARY KEY (id);


--
-- Name: atelier_complicationelement atelier_complicationelement_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_complicationelement
    ADD CONSTRAINT atelier_complicationelement_pkey PRIMARY KEY (id);


--
-- Name: atelier_fabric atelier_fabric_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_fabric
    ADD CONSTRAINT atelier_fabric_pkey PRIMARY KEY (id);


--
-- Name: atelier_minimalstyle atelier_minimalstyle_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_minimalstyle
    ADD CONSTRAINT atelier_minimalstyle_pkey PRIMARY KEY (id);


--
-- Name: atelier_order_allowance_discount atelier_order_allowance__order_id_allowancediscou_5826d5f9_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_allowance_discount
    ADD CONSTRAINT atelier_order_allowance__order_id_allowancediscou_5826d5f9_uniq UNIQUE (order_id, allowancediscount_id);


--
-- Name: atelier_order_allowance_discount atelier_order_allowance_discount_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_allowance_discount
    ADD CONSTRAINT atelier_order_allowance_discount_pkey PRIMARY KEY (id);


--
-- Name: atelier_order_complication_elements atelier_order_complicati_order_id_complicationele_acbe3162_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_complication_elements
    ADD CONSTRAINT atelier_order_complicati_order_id_complicationele_acbe3162_uniq UNIQUE (order_id, complicationelement_id);


--
-- Name: atelier_order_complication_elements atelier_order_complication_elements_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_complication_elements
    ADD CONSTRAINT atelier_order_complication_elements_pkey PRIMARY KEY (id);


--
-- Name: atelier_order atelier_order_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order
    ADD CONSTRAINT atelier_order_pkey PRIMARY KEY (id);


--
-- Name: atelier_product atelier_product_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_product
    ADD CONSTRAINT atelier_product_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: atelier_order_allowance_discount_allowancediscount_id_6483c11d; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_allowance_discount_allowancediscount_id_6483c11d ON public.atelier_order_allowance_discount USING btree (allowancediscount_id);


--
-- Name: atelier_order_allowance_discount_order_id_2896ddfb; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_allowance_discount_order_id_2896ddfb ON public.atelier_order_allowance_discount USING btree (order_id);


--
-- Name: atelier_order_client_id_a542c9de; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_client_id_a542c9de ON public.atelier_order USING btree (client_id);


--
-- Name: atelier_order_complication_complicationelement_id_aad15a47; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_complication_complicationelement_id_aad15a47 ON public.atelier_order_complication_elements USING btree (complicationelement_id);


--
-- Name: atelier_order_complication_elements_order_id_12d03d55; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_complication_elements_order_id_12d03d55 ON public.atelier_order_complication_elements USING btree (order_id);


--
-- Name: atelier_order_fabric_id_5a54eefd; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_fabric_id_5a54eefd ON public.atelier_order USING btree (fabric_id);


--
-- Name: atelier_order_product_id_73f0bb1c; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_order_product_id_73f0bb1c ON public.atelier_order USING btree (product_id);


--
-- Name: atelier_product_minimal_style_id_d81fef44; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX atelier_product_minimal_style_id_d81fef44 ON public.atelier_product USING btree (minimal_style_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: dbdev
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: atelier_order_allowance_discount atelier_order_allowa_allowancediscount_id_6483c11d_fk_atelier_a; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_allowance_discount
    ADD CONSTRAINT atelier_order_allowa_allowancediscount_id_6483c11d_fk_atelier_a FOREIGN KEY (allowancediscount_id) REFERENCES public.atelier_allowancediscount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order_allowance_discount atelier_order_allowa_order_id_2896ddfb_fk_atelier_o; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_allowance_discount
    ADD CONSTRAINT atelier_order_allowa_order_id_2896ddfb_fk_atelier_o FOREIGN KEY (order_id) REFERENCES public.atelier_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order atelier_order_client_id_a542c9de_fk_atelier_client_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order
    ADD CONSTRAINT atelier_order_client_id_a542c9de_fk_atelier_client_id FOREIGN KEY (client_id) REFERENCES public.atelier_client(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order_complication_elements atelier_order_compli_complicationelement__aad15a47_fk_atelier_c; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_complication_elements
    ADD CONSTRAINT atelier_order_compli_complicationelement__aad15a47_fk_atelier_c FOREIGN KEY (complicationelement_id) REFERENCES public.atelier_complicationelement(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order_complication_elements atelier_order_compli_order_id_12d03d55_fk_atelier_o; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order_complication_elements
    ADD CONSTRAINT atelier_order_compli_order_id_12d03d55_fk_atelier_o FOREIGN KEY (order_id) REFERENCES public.atelier_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order atelier_order_fabric_id_5a54eefd_fk_atelier_fabric_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order
    ADD CONSTRAINT atelier_order_fabric_id_5a54eefd_fk_atelier_fabric_id FOREIGN KEY (fabric_id) REFERENCES public.atelier_fabric(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_order atelier_order_product_id_73f0bb1c_fk_atelier_product_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_order
    ADD CONSTRAINT atelier_order_product_id_73f0bb1c_fk_atelier_product_id FOREIGN KEY (product_id) REFERENCES public.atelier_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: atelier_product atelier_product_minimal_style_id_d81fef44_fk_atelier_m; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.atelier_product
    ADD CONSTRAINT atelier_product_minimal_style_id_d81fef44_fk_atelier_m FOREIGN KEY (minimal_style_id) REFERENCES public.atelier_minimalstyle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dbdev
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

