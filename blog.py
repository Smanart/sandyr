import streamlit as st  

page_bg_img = """
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://images.unsplash.com/photo-1486512696050-930b2d89cb4c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D);
        background-size: cover;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }
    [data-testid="stSidebar"] {
        background-image: url(https://images.unsplash.com/photo-1513553404607-988bf2703777?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D);
        background-size: cover;    
    }
</style>
"""

custom_corner = """
<style>
    #rcorner {
        border-radius: 0px;
        background: #FFFFFF80;
        padding: 21px; 
        width: 287px;
        height: 170px;
        color: #000000;
    }
</style>
"""

font_change = """
<style>
    h1 {
        font-family: 'Rubik Mono One', Sans-serif;
        color: #000000;
    }
    h2 {
        font-family: 'Times New Roman', Sans-serif;
        font-size: 30px;
        color: #FFFFFF;
    }
    h3 {
        font-family: 'Times New Roman', Sans-serif;
        font-size: 25px
        text-align: center;
        color: #FFFFCC
    }
</style>
"""

custom_text = """
<style>
    .custom-color {
        color: #FFFFFF;
        text-align: justify;
    }
</style>
"""

custom_align = """
<style>
    .custom_text {
        color: #FFFFFF;
    }
</style>
"""


st.set_page_config(page_title="""Exploring Life's Tapestry""", page_icon=':heart:')


st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(custom_corner, unsafe_allow_html=True)
st.markdown(font_change, unsafe_allow_html=True)
st.markdown(custom_text, unsafe_allow_html=True)
st.markdown(custom_align, unsafe_allow_html=True)

with st.container():
    st.sidebar.image('about5.png')
    st.sidebar.image('author1.png') 
    st.sidebar.image('sandyr1.png')  
    st.sidebar.markdown("""<p id="rcorner">A student from Surigao Del Norte State University (SNSU) and Currently pursuing Bachelor of Science in Computer Engineering (BSCpE)</p>""", unsafe_allow_html=True)

    st.sidebar.write('---')

    st.sidebar.markdown('*<h2>Contact Information:</h2>*', unsafe_allow_html=True)
    st.sidebar.markdown("""*<p class="custom-color">Gmail: sandyrmanliguis2@gmail.com</p>*""", unsafe_allow_html=True)
    st.sidebar.markdown("""*<p class="custom-color">Facebook: https://www.facebook.com/sandyrmanliguis04</p>*""", unsafe_allow_html=True)

with st.container():
        st.image('trans4.png')
        st.write("""<p class="custom-color"">From my earliest days as a child, my life has been rich with a multitude of interests and memorable childhood experiences. As I ventured into the expansive realm of the world, the diversity of experiences encouraged me to embrace life in its entirety, urging me to live each moment to the fullest. This blog serves as a curated collection, chronicling my journey of growth in this magnificent world. Join me as I navigate the tapestry of my past and present, sharing the valuable lessons, cherished memories, and the vibrant essence of a life well-lived.</p>""", unsafe_allow_html=True)

         
st.write('---')

with st.container():
    st.write('---')
    st.markdown('<h2>The Spark of Curiosity: A Childhood Unveiled</h2>', unsafe_allow_html=True)

    st.markdown("""<p class="custom-color">
                    As a child, the simple joy of playing outside with my friends was an integral part of my upbringing. Our days were filled with boundless adventures, as we fearlessly explored the world around us. From chasing after birds to observing tiny insects, and even attempting to catch fishes in the nearby canals, each escapade was a treasure trove of discovery. Despite the occasional bumps and bruises from our daring exploits, those minor cuts were mere badges of honor that we wore proudly. They taught me resilience and the valuable lesson that some scraped knees were a small price to pay for the thrill of exploration and camaraderie.
                    </p>""", unsafe_allow_html=True)
    st.markdown("""<p class="custom-color">
                    Amidst the backdrop of our outdoor escapades, another passion quietly took root in my heart the love for doodling. Whether armed with a scrap of paper or adorning the margins of my school notebooks, I found a canvas for my boundless imagination. Early doodles, though simple, became vibrant additions to the narratives of our adventures, each stroke of color a testament to the budding artist within. Those carefree days of exploration and creativity shaped not only my childhood but also laid the foundation for a lifelong appreciation of nature and art. The echoes of laughter and the vibrant hues of my early doodles continue to resonate, reminding me of a time when the world was an endless playground, and every stroke of the pencil held the promise of a new adventure.</p>""", unsafe_allow_html=True)

    st.markdown('<h2>A Journey into the Open World</h2>', unsafe_allow_html=True)
    st.markdown("""<p class="custom-color">
                    These escapades and doodling sessions were more than just play; 
                    they were profound lessons in resilience and camaraderie. Every scraped knee was a small victory, 
                    revealing my capacity for toughness. The world outside became our expansive classroom, 
                    teaching us about nature and instilling the courage to face challenges.
                    The laughter of those carefree days echoed in the fields, creating memories that still bring a smile. 
                    Looking back, the simple joys of playing outside and doodling created a lasting bond, 
                    reminding me of the happiness found in the little things and the adventures shared with friends. 
                    These early experiences laid the foundation for a journey into the open world, where curiosity, 
                    friendship, and creativity intertwined to shape the person I am today.
                </p>""",  unsafe_allow_html=True)


st.write('---')

with st.container():
        st.write('---')
        st.markdown("<h2>Artistic Mind of a Young Artist</h2>", unsafe_allow_html=True)

        st.write("""<p class="custom-color">As a young artist, there's a crucial aspect of my creative journey that deserves attention 
                     — the interplay between impatience and perfectionism. In my early years, 
                    impatience and a penchant for perfection were constant companions. 
                    My younger self would eagerly anticipate a flawless masterpiece right from the start, 
                    only to be met with disappointment when the reality fell short of my grand expectations. 
                    This frustration often led to the abandonment of projects; I would cease working on them 
                    simply because they didn't align with the perfect image I had envisioned. 
                    The discrepancy between the imagined perfection and the perceived shortcomings halted the completion of several pieces.
                </p>""",  unsafe_allow_html=True) 
        st.write("""<p class="custom-color">During this phase, my mind was brimming with ideas, yet my efforts were disproportionately minimal. 
                    I aspired to create masterpieces effortlessly, unaware that artistic excellence requires dedication, 
                    practice, and the acceptance of imperfections along the way. My younger self expected every piece to 
                    be perfect without fully grasping the necessity of hard work and the iterative nature of the creative process.
                </p>""",  unsafe_allow_html=True)
        st.write("""<p class="custom-color">The realization dawned that there is a plethora of ideas within an artist's mind, 
                    but attempting to bring them all to life in a single burst of creativity is neither 
                    necessary nor practical. I've learned to be patient, savoring my hobby and letting creativity 
                    flow at its own pace. This shift in mindset has not only contributed to a more enjoyable 
                    artistic process but has also allowed me to appreciate the beauty found in the journey itself.
                </p>""",  unsafe_allow_html=True)
        st.write("""<p class="custom-color">The evolution from a young artist expecting immediate perfection to one who 
                    values the journey and growth within each piece has been transformative. While the echoes of 
                    impatience and perfectionism persist, I now view them as catalysts for improvement rather than 
                    impediments to my creative expression. Today, I understand that the essence of art lies not only 
                    in the pursuit of perfection but in the resilience to persevere through the creative process, 
                    embracing imperfections as stepping stones toward artistic excellence.
                </p>""", unsafe_allow_html=True)
 

st.write('---')         
             
with st.container():
        st.write('---') 
        st.markdown('<h2>Navigating the Athletic Odyssey of a Dedicated Student</h2>', unsafe_allow_html=True)
        
        st.write("""<p class="custom-color">Beyond my passion for drawing, my journey through athletics 
                        has been a profound and transformative experience. My foray into 
                        sports began during my elementary years in 2016 when I explored 
                        activities like badminton and table tennis. Despite putting in 
                        considerable effort, victory eluded me in those early competitions. 
                        However, setbacks became stepping stones, teaching me resilience 
                        and the value of perseverance.
                    </p>""",  unsafe_allow_html=True)
        st.write("""<p class="custom-color">In 2017, a pivotal moment occurred when I enrolled in a karate school. 
                    Half a year of dedicated training culminated in a significant triumph—I 
                    secured a Gold and Silver medal in a tournament, earning the coveted yellow belt. 
                    This achievement ignited a fervent passion for martial arts within me. Unfortunately, 
                    financial constraints forced a temporary pause in my karate journey, but the fire 
                    within continued to burn.
                </p>""",  unsafe_allow_html=True)
        st.write("""<p class="custom-color">In 2018, as a grade 8 student, I found solace and purpose in Taekwondo. 
                    The discipline demanded my dedication, and I embraced the challenges, 
                    relishing the pain and sweat of each training session. The road was challenging, 
                    marked by numerous losses, but perseverance paid off, and I clinched a 
                    gold medal in a tournament during my senior year. However, the transition 
                    to high school and, subsequently, college brought about a mental and 
                    emotional shift. Martial arts had been my anchor, a source of significance, 
                    and its absence left a void within me.
                </p>""", unsafe_allow_html=True)
        st.write("""<p class="custom-color">Recognizing the need for a new outlet, I turned to cycling in 2022. 
                    Cycling not only provided a means of staying physically active but also 
                    allowed me to control the time and place of my training, accommodating the 
                    demands of my studies. This shift taught me a crucial life lesson — the 
                    importance of adaptability and finding alternative paths when faced with 
                    obstacles. While my martial arts journey took a pause, cycling became a 
                    rejuvenating hobby, a testament to the resilience of the human spirit.
                </p>""",  unsafe_allow_html=True)
        st.write("""<p class="custom-color">Life is a series of transitions, and adaptability is key. Whether it's 
                overcoming financial challenges, shifting priorities, or discovering new 
                hobbies, each phase contributes to personal growth. As I set my sights 
                on participating in cycling competitions, I carry with me the wisdom gained 
                from my varied athletic pursuits—a testament to the indomitable spirit 
                that continues to evolve and thrive.
                </p>""",  unsafe_allow_html=True)

st.write('---')

with st.container():
    st.write('---')
    st.markdown('<h2>A Journey of Discovery, Love, and Lessons on the Open Road</h3>', unsafe_allow_html=True)
    
    st.write("""<p class="custom-color">As I embark on my cycling journeys, the realization unfolds that the world is an expansive tapestry, transcending the mere designation of a planet that we inhabit. Each turn of the pedal unveils the diverse landscapes, the changing seasons, and the vibrant cultures that collectively form the intricate mosaic of our shared existence. The rhythmic cadence of my bicycle wheels becomes a harmonious echo of my connection with the Earth, reminding me that this world is not just a place we inhabit but a living, breathing entity that demands our appreciation and care.
              </p>""",  unsafe_allow_html=True)
    st.write("""<p class="custom-color">Cycling has become my avenue for firsthand experiences, a dynamic portal through which I witness the beauty of nature and the resilience of communities. It's not merely a mode of transportation but a conduit for exploration and discovery. As I navigate through winding paths and open roads, the wind in my hair and the scenery evolving around me, I'm reminded of the profound importance of cherishing these moments—of being present in the journey rather than fixated on the destination.
              </p>""",  unsafe_allow_html=True)
    st.write("""<p class="custom-color">
                    In the approaching threshold of adulthood, the lessons learned extend far beyond the physical landscapes traversed. Love, in its myriad forms, has revealed itself as an intricate dance between vulnerability and strength, connection and autonomy. The pragmatic realm of money has brought forth its own set of lessons, teaching me about financial responsibility, the pursuit of goals, and the delicate balance between material aspirations and personal fulfillment.
                </p>""",  unsafe_allow_html=True)
    st.markdown("""<p class="custom-color">
                    Life, in its entirety, has become a canvas painted with experiences, emotions, and the unpredictable twists of fate. The 'etc.' in my contemplation expands to encompass a spectrum of learnings—from understanding the importance of self-discovery to grappling with the complexities of human relationships. Each revolution of the bicycle pedals not only propels me forward on the physical plane but also propels my understanding of the world, shaping my evolving narrative as I approach the horizon of adulthood. The future, with its uncertainties and promises, awaits, and I carry forward the lessons learned from the open road—a tapestry woven with threads of appreciation, resilience, and a profound sense of interconnectedness with the world around me.
                </p>""",  unsafe_allow_html=True)
st.write('---')
st.write('---')

with st.container():
    st.image('transp3.png')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('drw.jpg') 
        st.image('drw2.jpg')   
        st.image('drw3.jpg')   
    with col2:
        st.image('taekwondo.jpg')   
        st.image('taekwondo2.jpg')   
        st.image('taekwondo3.jpg')   
    with col3:    
        st.image('bike.jpg')   
        st.image('bike2.jpg')   
        st.image('bike3.jpg')