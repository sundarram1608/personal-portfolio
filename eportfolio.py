import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(page_title="Sundar Ram Subramanian: Portfolio", layout="wide")



st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# HEADER NAVIGATION
# -----------------------------
st.markdown(
            """
            <style>
              /* Remove Streamlit's default top padding so our bar can sit at the very top */
              .block-container { padding-top: 4.8rem !important; }

              /* Hide Streamlit's own top header bar so it doesn't push our nav down */
              /*[data-testid="stHeader"] { display: none; }*/
              
              [data-testid="stToolbar"] { display: none; } /* optional; removes the floating toolbar */
              

              /* Fixed nav bar at absolute top */
              .top-nav-wrap{
                              position: fixed;
                              top: 0;                 /* <-- RIGHT AT THE TOP */
                              left: 0;
                              right: 0;
                              z-index: 999999;
                              background: color(srgb 0.057 0.067 0.0882);
                              border-bottom: 1px solid rgba(54,82,102,0.12);
                              padding: 1px 1px;
                              width: 100%;
                              display: flex;
                            }

              /* Branding on the left */
              .top-nav-brand{
                              display: flex;
                              justify-content: flex-start; /* LEFT */
                              gap: 20px;
                              align-items: initial;
                              max-width: 1300px;
                              margin-left: 50px;
                              font-size: 1rem;
                              font-weight: 500;
                              width: 50%;
                            }

              .top-nav-links{
                              display: flex;
                              justify-content: flex-end; /* RIGHT */
                              gap: 20px;
                              align-items: center;
                              max-width: 1300px;
                              margin-right: 50px;
                              font-size: 0.9rem;
                              font-weight: 350;
                              width: 50%;
                            }

              /* Blue links, no underline */
              .top-nav-links a{
                                  color: #fcfcfc;
                                  text-decoration: none !important;
                                }
              .top-nav-links a:hover{
                                        text-decoration: none;
                                        color: #f5c542;
                                      }

              /* Prevent anchor jumps from hiding headings under the fixed nav */
              h2 { scroll-margin-top: 150px; }
              
                /* Branding on the right */
              .brand{
                      margin-left: 18px;          /* spacing from links */
                      font-weight: 700;
                      letter-spacing: 0.08em;
                      color: #ffffff;
                      font-size: 1.05rem;
                      padding: 6px 10px;
                      user-select: none;
                    }
                    
              .brand:hover {
                            background: rgba(255, 255, 255, 0.15);
                          }
              .highlight-name {
                                background: -webkit-linear-gradient(30deg, #3b82f6, #14b8a6);
                                -webkit-background-clip: text;
                                -webkit-text-fill-color: transparent;
                                }
                                
              /* Gradient button style (matches highlight-name colors) */
              .cta-button {
                            display: inline-block;
                            padding: 14px 28px;
                            margin: 20px 12px 0 12px;
                            font-size: 1.1rem;
                            font-weight: 600;
                            text-decoration: none !important;

                            /* Button background */
                            background: linear-gradient(45deg, #3b82f6, #14b8a6);
                            border-radius: 10px;

                            /* FORCE white text */
                            color: #ffffff !important;
                            -webkit-text-fill-color: #ffffff !important;

                            transition: transform 0.2s ease, box-shadow 0.2s ease;
                          }

              .cta-button:hover {
                                  transform: translateY(-2px);
                                  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
                                }

/* --- Two-column timeline container spacing --- */
              .timeline-title{
                                font-size: 1.4rem;
                                font-weight: 650;
                                margin: 0 0 14px 0;
                                    color: #fcfcfc;
                                    text-align: center;
                                  }
              /* --- Timeline base --- */
              .timeline{
                          position: relative;
                          padding-left: 24px; /* space for the line + dots */
                          margin-top: 6px;
                        }

              .timeline:before{
                                content: "";
                                position: absolute;
                                left: 8px;
                                top: 0;
                                bottom: 0;
                                width: 2px;
                                background: rgba(255,255,255,0.20);
                                border-radius: 2px;
                              }

              /* --- Each item --- */
              .t-item{
                        position: relative;
                        margin: 0 0 20px 10px;
                        padding: 14px 14px 14px 16px;
                        background: transparent;
                        border: 1px solid rgba(255,255,255,0.12);
                        border-radius: 14px;
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                      }

            /* Academic badge dot (glow ring + gradient inner + white cap icon) */
              .t-item.academic:before{
                                        content: "";
                                        position: absolute;
                                        left: -39px;
                                        top: 14px;
                                        width: 25px;
                                        height: 25px;
                                        border-radius: 999px;

                                        /* 🔑 MULTI-LAYER BACKGROUND (icon on top, gradient below) */
                                        background:
                                          url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M12 3 1 9l11 6 9-4.91V17h2V9L12 3zm-6.5 9.09V16c0 1.66 3.13 3 6.5 3s6.5-1.34 6.5-3v-3.91L12 16l-6.5-3.91z'/%3E%3C/svg%3E")
                                            center / 20px 20px no-repeat,
                                          linear-gradient(45deg, #3b82f6, #14b8a6);

                                        /* subtle depth (your preferred look) */
                                        box-shadow:
                                          0 0 0 8px rgba(59,130,246,0.20),
                                          0 0 10px rgba(20,184,166,0.35);
                                      }
            
              /* Work badge dot */
              .t-item.work:before{
                                    content: "";
                                    position: absolute;
                                    left: -39px;
                                    top: 14px;
                                    width: 25px;
                                    height: 25px;
                                    border-radius: 999px;

                                    /* 🔑 MULTI-LAYER BACKGROUND (icon on top, gradient below) */
                                    background:
                                      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M10 2h4a2 2 0 0 1 2 2v2h4a2 2 0 0 1 2 2v3H2V8a2 2 0 0 1 2-2h4V4a2 2 0 0 1 2-2zm4 4V4h-4v2h4zM2 13h20v5a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-5z'/%3E%3C/svg%3E")
                                        center / 18px 18px no-repeat,
                                      linear-gradient(45deg, #3b82f6, #14b8a6);

                                    /* subtle depth (your preferred look) */
                                    box-shadow:
                                      0 0 0 8px rgba(59,130,246,0.20),
                                      0 0 10px rgba(20,184,166,0.35); 
                                  }
              /* --- Item content --- */
              .t-date{
                        font-size: 1rem;
                        opacity: 1.85;
                        margin-bottom: 6px;
                        font-weight: 600;
                      }

              .t-role{
                        font-size: 1.3rem;
                        font-weight: 800;
                        margin: 0 0 4px 0;
                        color: #7fffe1;/*55B4A8*/
                      }

              .t-org{
                      font-size: 1.1rem;
                      font-weight: 700;
                      margin: 0 0 8px 0;
                      color: #4F83EB;
                    }

              .t-desc{
                        font-size: 0.95rem;
                        line-height: 1.45;
                        color: #fcfcfc;
                        margin: 0;
                        text-align: justify;
                      }
                      
              .highlight-key{
                              font-style: italic;
                              text-decoration: underline;
                              text-underline-offset: 3px;
                            }
                            
              .t-tags{
                        margin-top: 10px;
                        display: flex;
                        flex-wrap: wrap;
                        gap: 8px;
                      }

              .t-tag{
                      font-size: 0.9rem;
                      padding: 4px 10px;
                      border-radius: 999px;
                      border: 1px solid rgba(255,255,255,0.18);
                      background: linear-gradient(45deg, #3b82f6, #14b8a6);
                      color: #fcfcfc;
                      font-weight: 500;
                    }
              .t-link{
                        color: #7FFFE1;                 /* bright, readable */
                        text-decoration: underline;
                        text-underline-offset: 3px;
                        font-weight: 600;
                      }

              .t-link:hover{
                              color: #f5c542;
                            }

              /* Make sure the two columns don't look cramped on smaller widths */
              @media (max-width: 900px){
                                        .timeline-title{ text-align: center; }
                                      }
              /* GPA pill */
              .gpa-pill{
                          display: inline-block;
                          padding: 4px 12px;
                          margin-top: 8px;
                          margin-bottom: 8px;
                          margin-right: 8px;
                          font-size: 1rem;
                          font-weight: 600;

                          color: #fcfcfc;
                          background: transparent;

                          border: 1px solid rgba(255,255,255,1);
                          border-radius: 999px;
                        }
                                                                                                              
              /* Social icon buttons */
              .social-buttons{
                                display: flex;
                                justify-content: center;
                                gap: 18px;
                                margin-top: 2px;
                              }

              .social-btn{
                          width: 46px;
                          height: 46px;
                          border-radius: 50%;
                          display: flex;
                          align-items: center;
                          justify-content: center;
                          text-decoration: none;
                          background: #5A5A5A;                 /* WHITE background */
                          border: 1px solid rgba(0,0,0,0.15); 
                        }

              .social-btn:hover{
                                  transform: translateY(-2px);
                                  background: #f5c542;
                                  box-shadow: 0 6px 18px rgba(0,0,0,0.4);
                                }

              /* Icon sizing */
              .social-btn img{
                                width: 30px;
                                height: 30px;
                              /* grey tone */
                                filter: brightness(0);                              }

    /* ---------- MOBILE RESPONSIVE OVERRIDES ---------- */
    @media (max-width: 768px){

      /* Reduce global padding and avoid horizontal scroll */
      html, body { overflow-x: hidden; }
      .block-container { padding-top: 4.2rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }

      /* Nav: stack, reduce margins, allow wrap */
      .top-nav-wrap{
        padding: 8px 10px !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
      }
      .top-nav-brand{
        width: 100% !important;
        margin-left: 0 !important;
        justify-content: center !important;
        align-items: center !important;
      }
      .top-nav-links{
        width: 100% !important;
        margin-right: 0 !important;
        justify-content: center !important;
        flex-wrap: wrap !important;
        gap: 12px !important;
        font-size: 0.95rem !important;
      }

      /* HERO: scale down huge typography */
      #home h1 { font-size: 2.4rem !important; line-height: 1.1 !important; }
      #home h3 { font-size: 1.3rem !important; }
      #home h4 { font-size: 1.0rem !important; line-height: 1.4 !important; padding: 0 8px !important; }

      /* CTA buttons: full width on mobile */
      .cta-button{
        display: block !important;
        width: 100% !important;
        max-width: 420px !important;
        margin: 12px auto 0 auto !important;
        text-align: center !important;
        padding: 12px 18px !important;
        font-size: 1rem !important;
      }

      /* Timeline: tighten spacing */
      .timeline{ padding-left: 18px !important; }
      .timeline:before{ left: 6px !important; }
      .t-item{ margin-left: 6px !important; padding: 12px !important; }
      .t-item.academic:before, .t-item.work:before{
        left: -32px !important;
        width: 22px !important;
        height: 22px !important;
        top: 14px !important;
        background-size: 16px 16px, auto !important;
      }
      .t-role{ font-size: 1.1rem !important; }
      .t-org{ font-size: 1.0rem !important; }
      .t-desc{ font-size: 0.95rem !important; text-align: left !important; }

      /* Pills/tags wrap nicely */
      .t-tags{ gap: 6px !important; }
      .t-tag{ font-size: 0.85rem !important; padding: 3px 9px !important; }

      /* Social buttons: smaller */
      .social-btn{ width: 42px !important; height: 42px !important; }
      .social-btn img{ width: 26px !important; height: 26px !important; }
    }

            </style>""",
            unsafe_allow_html=True #<a href="#academic-journey">Academic Journey</a>
          )


st.markdown(
            """            
            <div class="top-nav-wrap">
              <div class="top-nav-brand">
                <h2 href="#brand"><span class="highlight-name">RAM</span></h2>
              </div>
            <div class="top-nav-links">             
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#journey">Journey</a>
                <a href="#projects">Projects</a>
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
              </div>
            </div>
            """, unsafe_allow_html=True)

# <a href="#home">Home</a>
# -----------------------------
# HOME
# -----------------------------
st.markdown(
              """            
              <div id="home" style="text-align:center; padding: 60px 0 100px 0;">
                  <h1 style="font-size:6rem; margin-bottom:4px;">
                      Sundar Ram Subramanian
                  </h1>
                  <h3 style="font-weight:600; color:#fcfcfc; font-size:3rem;">
                      <span class="highlight-name">Data Scientist</span><span class="highlight-name"> & </span><span class="highlight-name">Machine Learning Engineer</span>
                  </h3>               
                  <h4 style="font-size: 2rem; font-weight: 300;">
                      Leveraging Deep Learning and Information Retrieval techniques 
                      <div>
                      <span class="highlight-name" style="font-weight: 500;">
                      to decipher patterns into purpose and causal relationships </span></div>
                      for meaningful impact and global well-being!
                  </h4>
              </div>
              """,
              unsafe_allow_html=True,
          )

st.markdown(
              """         
              <div style="text-align:center; padding-bottom: 70px;">   
                  <!-- Call-to-action buttons -->
                  <div style="margin-top: 30px;">
                      <a href="#projects" class="cta-button">View My Work</a>
                      <a href="#contact" class="cta-button">Get In Touch</a>
                  </div>
              </div>
              """,
              unsafe_allow_html=True,
          )
st.write("")
st.write("")
st.write("")
st.write("")

# -----------------------------
# ABOUT
# -----------------------------
st.markdown(
            """            
            <div id="about" style="text-align:center; padding: 60px 0 40px 0; scroll-margin-top: 90px;">
            <h2>About me</h2>
            </div>
            """,
            unsafe_allow_html=True,
         )

# Two side-by-side containers
col1, col2 = st.columns([1, 2], vertical_alignment="top")

with col1:
    st.image("images/profilepicture.jpg", width="content")
    
with col2:      
  st.markdown(
              """
              <div style="font-size: 1.1rem; line-height: 1.2; text-align: justify;">
                  <p>
                  Based in Tucson, Arizona, I am <span style="color: #f5c542; font-weight: 500;">graduating May 2026</span> with a Master’s in Machine Learning from the University of Arizona.
                  </p>
                  <p>
                  My career began with Titan Company Limited as Lead – New Product Development, where I transformed data into
                  actionable insights <span class="highlight-name" style="font-weight: 500;">driving business growth and innovation</span>.
                  My analytical acumen identified a <span class="highlight-name" style="font-weight: 500;">₹1B opportunity</span>, resulting in the first-ever skeletal quartz watch for the Sonata brand, driving a paradigm shift in brand perception. 
                  I further built robust decision support systems that achieved a <span class="highlight-name" style="font-weight: 500;">75–80% reduction in costs and manufacturing lead times</span>. 
                  These experiences led me to formalize my data science expertise through a Post Graduate Program in Data Science & Business Analytics from The University of Texas at Austin. 
                  </p>
                  <p>
                  Quick to notice my potential, Titan inducted me into its <span class="highlight-name" style="font-weight: 500;">Young Leadership Program (top 12%)</span> with a
                  sponsored PG in Business Management from XLRI. During this program, I led initiatives <span class="highlight-name" style="font-weight: 500;">product attribution & consumer analytics</span>, optimizing inventory and driving <span class="highlight-name" style="font-weight: 500;">29% sales growth</span> in Titan Wedding Jewelry.
                  Subsequently, I spearheaded Titan’s Data Centre of Excellence, building production-grade <span class="highlight-name" style="font-weight: 500;">ML and LLM pipelines</span> along with <span class="highlight-name" style="font-weight: 500;">Streamlit dashboards</span> that delivered 20–25% improvements in measurable business outcomes, ultimately motivating
                  my pursuit of a Master’s in Machine Learning at the University of Arizona, where I focus on Deep Learning and Information Retrieval for Natural Language Processing, Computer Vision and Music applications.
                  </p>
                  <p>
                  I am driven to apply these skills to the most complex business challenges, spanning robust <span class="highlight-name" style="font-weight: 500;">deep learning pipelines for Multimodal applications</span>, as well as inferring <span class="highlight-name" style="font-weight: 500;">causal relationships in advanced analytics that translate data into actionable insights.</span></div>
                  </p>
              """,
                  unsafe_allow_html=True
              )

st.write("")
st.write("")
st.write("")
st.write("")


# -----------------------------
# JOURNEY
# -----------------------------
st.markdown(
              """            
              <div id="journey" style="text-align:center; padding: 60px 0 40px 0; scroll-margin-top: 90px;">
              <h2>Journey</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )
#Two side-by-side containers for Industry and Academics
left, right = st.columns(2, vertical_alignment="top")

# -----------------------------
# INDUSTRY JOURNEY
# -----------------------------

with left:
  # with st.container(border=False, height=800):
    st.markdown("<div class='timeline-title'>Industry</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="timeline">

          <div class="t-item work">
            <div class="t-date">Oct 2023 - Jul 2025</div>
            <div class="t-role">Data Science & Advanced Analytics</div>
            <div class="t-org">Titan Company Limited</div>
            <p class="t-desc">
              Spearheaded the Data Centre of Excellence, leveraging Generative AI & Machine Learning Models 
              to build & deploy Deep Learning pipelines and web applications for Analytics use cases with Python & SQL.
            </p>
            <p class="t-desc">
              &nbsp;
            </p>
            <p class="t-desc">
              <span class="highlight-key">Sentiment Analytics (GenAI):</span> Developed LLM-powered sentiment analysis web application
              using OpenAI’s API and Streamlit for the Marketing and Merchandise teams that delivered competitive insights, 
              improving targeted campaigning and product planning outcomes by ~ 10%.
            </p>
            <p class="t-desc">
              &nbsp;
            </p>
            <p class="t-desc">
              <span class="highlight-key">Merchandise Copilot (GenAI):</span> Built an LLM-driven pipeline using OpenAI’s APIs to analyze textual and audio feedback from 
              non-purchasers, enabling the Merchandise team to optimize product assortment and drive ~ 8 to 10% sales uplift per stored
            </p>
            <p class="t-desc">
              &nbsp;
            </p>            
            <p class="t-desc">
              <span class="highlight-key">Product Annotation and Content generation (GenAI):</span> 
              Delivered an LLM-driven pipeline using OpenAI’s API to extract prominent design elements from jewelry images, 
              automating product description generation and reducing manual effort by ~30 minutes per product, while facilitating design analytics that increased portfolio diversity 
              and improved merchandise allocation decisions by ~5%.
            </p>
            <p class="t-desc">
              &nbsp;
            </p>
            <p class="t-desc">
              <span class="highlight-key">Customer Segmentation:</span> 
              Built a deep learning–based language classification pipeline to segment customers by mother tongue, integrated the model in ETL pipeline and automated mother tongue identification of new customers through AWS Glue,
              enabling targeted marketing initiatives that improved CRM customer engagement metrics by ~10%.
            </p>
            <p class="t-desc">
              &nbsp;
            </p>
            <p class="t-desc">
              <span class="highlight-key">Network Expansion:</span> Leveraged SQL to empower Retail team with insights on potential market opportunities.
            <p class="t-desc">
              &nbsp;
            </p>
            <p class="t-desc">
              <span class="highlight-key">Geo Spatial Analytics:</span> Leveraged Tableau for Geo Spatial Sales Analysis, to identify catchments with high customer affinity.
            </p>
            <div class="t-tags">
              <span class="t-tag">LLM Pipelines</span>
              <span class="t-tag">Gen AI</span>
              <span class="t-tag">Sentiment Analytics</span>
              <span class="t-tag">Merchandise Optimization</span>
              <span class="t-tag">Business Analytics</span>
              <span class="t-tag">Consumer Analytics</span>
              <span class="t-tag">Network Expansion</span>
              <span class="t-tag">Customer Segmentation</span>
            </div>
          </div>

          <div class="t-item work">
            <div class="t-date">Apr 2023 - Sep 2023</div>
            <div class="t-role">Merchandising</div>
            <div class="t-org">Titan Company Limited</div>
            <p class="t-desc">
              - Led product attribution and optimized inventory by demographic segments, which resulted 29% annual growth in wedding sales.
            </p>
            <p class="t-desc">
              - Analyzed sales & empowered product team with data-driven insights for introducing new products.
            </p>
            <div class="t-tags">
              <span class="t-tag">Product Annotation</span>
              <span class="t-tag">Sales Analysis</span>
              <span class="t-tag">Inventory Optimization</span>
              <span class="t-tag">Market Research</span>
            </div>
          </div>

          <div class="t-item work">
            <div class="t-date">Apr 2023 - Mar 2024</div>
            <div class="t-role">Young Leadership Program</div>
            <div class="t-org">Titan Company Limited</div>
            <p class="t-desc">
              - Identified amongst the top 12% of the company’s high-performing and emerging young talent with leadership potential. 
            </p>
            <p class="t-desc">
              - Fully sponsored with the Post Graduate Certificate in Business Management from XLRI.
            </p>
            <p class="t-desc">
              - Empowered the senior leadership of Jewelry Merchandising  and Digital Analytics Function with data-based decision support systems for several intriguing business challenges.
            </p>            
            <div class="t-tags">
              <span class="t-tag">Leadership</span>
              <span class="t-tag">Business Management</span>
              <span class="t-tag">Self-Reflection</span>
              <span class="t-tag">Merchandising</span>
              <span class="t-tag">Dashboarding</span>
            </div>
          </div>


          <div class="t-item work">
            <div class="t-date">Jul 2019 - Mar 2023</div>
            <div class="t-role">New Product Development</div>
            <div class="t-org">Titan Company Limited</div>
            <p class="t-desc">
              - Steered the product development of 600+ watch designs by effective analytics and project management for the Brand Sonata.
            </p>
            <p class="t-desc">
             - Formulated tailored product development milestones and aligned stakeholders to achieve 95% on-time design delivery.
            </p>
            <p class="t-desc">
              - Fostered innovation through extensive market research and implementation of SCAMPER technique, for a 1Bn watch market and introduced the first-ever branded skeletal quartz watch that enabled growth of >2K price band portfolio by 170%.
            </p>
            <p class="t-desc">
              - Empowered Top leadership with effective visual insights by analyzing the cost vs. Procurement matrix for optimal decision-making.
            </p>
            <p class="t-desc">
              - Reduced the lead time of proto-dial manufacturing from 45 to 10 days (77 %) by causal inferencing of manufacturing techniques that secured 13th rank in the National level Kaizen competition.
            </p>
            <p class="t-desc">
              - Established Lead time and product attributes correlation matrix, enabling watch production without prototype approval.
            </p>
            <div class="t-tags">
              <span class="t-tag">Product analytics</span>
              <span class="t-tag">Manufacturing analytics</span>
              <span class="t-tag">Kaizen</span>
              <span class="t-tag">Cost reduction</span>
              <span class="t-tag">Decision Support systems</span>
              <span class="t-tag">Product development</span>
              <span class="t-tag">Project Management</span>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# ACADEMIC JOURNEY
# -----------------------------

with right:
  # with st.container(border=False, height=1000):
    st.markdown("<div class='timeline-title'>Academics</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="timeline">

          <div class="t-item academic">
            <div class="t-date">Jun 2024 - May 2026</div>
            <div class="t-role">Masters in Information Science (Machine Learning)</div>
            <div class="t-org">University of Arizona</div>
            <p class="t-desc">
              <span class="highlight-key">Focus Area:</span> Building Deep Learning Pipelines, LLM Fine Tuning, Music Information Retrieval, NLP (SemEval tasks), & Computer Vision.
            </p>
            <div>
            <span class="gpa-pill">GPA: 4/4</span>
            <a href="https://eportfolio-sundar-ram-subramanian-masters-infosci-uofa.streamlit.app" target="_blank" class="t-link">↗︎Academic e-Portfolio</a>
            </div>
          </div>

          <div class="t-item academic">
            <div class="t-date">Sep 2023 - Aug 2024</div>
            <div class="t-role">Post Graduate Certification in Business Management</div>
            <div class="t-org">Xavier's School of Management (XLRI)</div>
            <p class="t-desc">
              <span class="highlight-key">Focus Area:</span> Business Management, International Business Development, Economics & Finance.
            </p>
            <div>
            <span class="gpa-pill">GPA: 6.52/8</span>
            </div>
          </div>

          <div class="t-item academic">
            <div class="t-date">Dec 2021 - Jan 2023</div>
            <div class="t-role">Post Graduate Program in Data Science and Business Analytics</div>
            <div class="t-org">University of Texas at Austin</div>
            <p class="t-desc">
              <span class="highlight-key">Focus Area:</span> Advanced Statistical Modelling, EDA, Supervised & Unsupervised Learning, Time Series Forecasting, SQL for Database, RFMA, MBA, Tableau & Dashboarding.
            </p>
            <div>
            <span class="gpa-pill">GPA: 3.6/4</span>
            <a href="https://eportfolio.mygreatlearning.com/sundar-ram-s" target="_blank" class="t-link">↗︎Academic e-Portfolio</a>
            </div>
          </div> 

        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")
st.write("")
st.write("")

# -----------------------------
# PROJECTS
# -----------------------------
st.markdown(
              """            
              <div id="projects" style="text-align:center; padding: 60px 0 40px 0; scroll-margin-top: 90px;">
              <h2 span style="alignment: center; color: #fcfcfc; font-weight: 700;font-size: 4rem;">Project Portfolio</h2>
              <span style="alignment: center; font-size: 1.2rem; color: #b3b5b4;">A portfolio of projects showcasing my skills in Machine Learning, Deep Learning, Gen AI, data & web app development.</span>
              </div>
              """,
              unsafe_allow_html=True,
          )

# -----------------------------
# FEATURED PROJECTS
# -----------------------------

st.markdown(
              """            
              <div id="projects" style="text-align:center; padding: 0 0 40px 0; scroll-margin-top: 90px;">
              <h2 style = "font-size: 2.8rem;">Featured Projects</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )


col1, col2, col3 = st.columns(3, vertical_alignment="top")

with col1:
  with st.container(border=True, height=550):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Google Review Analytics</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/gmbsentimentanalytics.jpg", use_container_width=False)
    selected_categories = ["Generative AI", "Web App Development", "Data Visualization", "Dashboarding"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_f1"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/Google-Review-Analytics.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                <a href="https://sentiment-analytics-g-reviews.streamlit.app/" target="_blank" class="t-link"> &nbsp;&nbsp;↗︎web application</a>
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    Leveraged OpenAI GPT models to translate unstructured customer reviews into actionable consumer insights. 
                    Also built a Streamlit-powered UI to visualize insights.
                """)
    
with col2:
  with st.container(border=True, height=550):

    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Semantic Evaluation</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/nlp.jpg", use_container_width=False)
    selected_categories = ["Deep Learning", "NLP", "Fine-Tuning", "Transfer Learning"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_f2"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/nlp_projects.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project involved solving certain Semeval shared tasks of 2019, 2020 and 2021, including Semantic Textual Similarity, OffensEval, MeasEval & ComVe. 
                    The tasks involved NLP techniques of Text Preprocessing, Text Similarity, Text Classification and Sequence Processing.
                    Concepts of GloVe (word embeddings), Word Mover's Distance, Cosine Similarities, Logistic Regression, Recurrent Neural Networks (RNNs), Convolutional Neural Networks (CNNs) and Fine-tuning of Pre-trained Language models like BERT and RoBERTa were applied.
                """)
with col3:
  with st.container(border=True, height=550):    
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Carnatic Music Raga Identification</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/carnatic.jpg", use_container_width=False)
    selected_categories = ["Deep Learning Pipeline", "Music Information Retrieval"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_f3"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/Carnatic-Music-Raga-Identification-using-MIR-and-Deep-Learning.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project leverages MIR techniques to extract and analyze Carnatic audio for 8 melakartha ragas, 
                    followed by building a fusion deep learning model (CNN+LSTM) for Raga classification.
                """)

# -----------------------------
# ALL PROJECTS
# -----------------------------

st.markdown(
              """            
              <div id="projects" style="text-align:center; padding: 40px 0 40px 0; scroll-margin-top: 90px;">
              <h2 style="font-size: 2.8rem;">All Projects</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )

col1, col2, col3 = st.columns(3, vertical_alignment="top")
with col1:
  with st.container(border=True, height=550):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Waste products classification</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/wasteclassification.jpg", use_container_width=False)
    selected_categories = ["Transfer Learning", "Computer Vision", "Fine-tuning"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a1"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/Transfer-Learning-and-Fine-Tuning---Image-Classification.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    Applied transfer learning using the VGG16 model to classify waste products as recyclable or organic.
                    The project involved preparing and preprocessing image data for ML task, fine-tuning the pre-trained VGG16 model to improve classification accuracy 
                    and evaluate the model’s performance.
                """)
    
with col2:
  with st.container(border=True, height=550):

    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Database Development and Management</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/dbms.jpg", use_container_width=False)
    selected_categories = ["DBMS", "Web App Development", "Analytics Dashboard", "Python-SQL integration"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a2"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/database_ui_development.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project presents the design and development of a comprehensive Data Management and Analytics System powered by MySQL and Python Streamlit.
                    Built on the Northwind dataset, that has been modified to suit academic nature of the project, 
                    this project transforms a traditional transactional database into a fully interactive platform capable of performing seamless data management operations (CRUD) and providing actionable business insights (Analytics). 
                    The system integrates a well-structured backend, a robust relational database, and an intuitive front-end interface to support a complete analytical workflow, including data ingestion, validation, CRUD operations, and visualization.
                """)
with col3:
  with st.container(border=True, height=550):    
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">German Bank Loan Prediction</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/loandefault.jpg", use_container_width=False)
    selected_categories = ["Machine Learning", "parametric models", "tree-based models", "ensemble models", "cross-validation", "hyperparameter tuning"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a3"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/classification_german_bank_default_prediction.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project predicts loan defaults in a German bank using historical data from customers. 
                    Several independent parametric & tree-based models were built and fine-tuned for hyperparameters along with identification of feature importance in different models to select the best model.
                    The dataset includes various attributes of customers who have taken loans, such as account balances, credit history, loan details, and personal demographics.
                """)

with col1:
  with st.container(border=True, height=550):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Visualizing Insurance Claims using Tableau</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/tableau.jpg", use_container_width=False)
    selected_categories = ["Tableau", "Story Boarding", "Data Visualization", "Business Intelligence"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a4"
                        )
    st.markdown(
                """
                <a href="https://public.tableau.com/app/profile/sundar.ram.s/viz/DVTProjectSundarRamS/Story1?publish=yes" target="_blank" class="t-link">↗︎ Tableau Dashboard</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project explored the art of problem-solving with the aid of visual analytics. 
                    Tableau’s data visualization tools were used to create interactive dashboards to provide high-level insights 
                    to the CEO of an Insurance company to drive the company's policymaking.
                """)
    
with col2:
  with st.container(border=True, height=550):

    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Statistical Data Analysis</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/stat.jpg", use_container_width=False)
    selected_categories = ["Business statistics", "Inferential statistics", "Hypothesis testing"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a5"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/statistical_data_analysis.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                This project explored 3 different datasets: Annual spending of wholesale distributor, survey of Students News Service at Clear Mountain State University and A & B type Asphalt Shingles’ moisture measurements of manufacturers of ABC Asphalt Shingles.
                The techniques of Fundamentals of Business statistics, Inferential statistics and Hypothesis testing were leveraged to answer specific business questions.
                """)

with col3:
  with st.container(border=True, height=550):    
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Forecasting Wine Sales for ABC Estate Wines company</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/tsf.jpg", use_container_width=False)
    selected_categories = ["Exponential Smoothing Models", "ARIMA/SARIMA Models", "Moving Average Models", "Time Series EDA"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a6"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/forecasting_time_series.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project performs exploratory data analysis on the sales data of ABC Estate Wines company in the 20th century, 
                    and builds various time series forecasting models including naive, simple average, exponential smoothing, ARIMA & SARIMA models to forecast future sales.""")

with col2:
  with st.container(border=True, height=550):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">Supply chain Analytics</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    st.image("images/sca.jpg", use_container_width=False)
    selected_categories = ["EDA", "Linear Models", "Ensemble Models", "Hyper Parameter tuning", "Data Visualization", "Business Intelligence"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"project_categories_a7"
                        )
    st.markdown(
                """
                <a href="https://github.com/sundarram1608/supply_chain_analytics.git" target="_blank" class="t-link">↗︎ Code Repo</a> - for more details.
                """,
                unsafe_allow_html=True,
              )
    st.markdown("""
                    This project involved building linear and ensemble regression models for an instant noodles company 
                    and optimizing them to streamline supply chain quantities, analyse demand patterns, and drive targeted advertising strategies 
                    to strengthen the bottom line.
                """)
    
# -----------------------------
# SKILLS
# -----------------------------
st.markdown(
              """            
              <div id="skills" style="text-align:center; padding: 60px 0 60px 0; scroll-margin-top: 90px;">
              <h2>Technical Skills</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )


skills_map = {
                "Machine Learning, AI & Data Science": ["NLP", "RAG", "LLM Fine-tuning", "Computer Vision", "Information Retrieval", "Prompt Engineering", "Business Analytics"],
                "Programming & Databases": ["Python", "SQL", "C++", "MySQL", "Amazon Redshift"],
                "ML & Data science Libraries": ["TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Transformers", "SciPy", "OpenCV", "YOLO", "Pandas", "Numpy", "Matplotlib", "Seaborn", "Boto3", "mysql"],
                "Cloud, MLOps & ML App Development": ["AWS SageMaker", "AWS S3", "JupyterLab", "Streamlit", "web applications", "dashboards"],
                "Analytics, BI Tools & Version Control": ["Tableau", "Power BI", "Advanced Excel", "KNIME", "Git", "GitHub"],
                "Product & Program Management": ["Product Development", "Project Management", "Stakeholder Management", "Vendor Management"],
            }

NUM_COLS = 6
cols = st.columns(NUM_COLS, vertical_alignment="top")

for i, (group_name, group_skills) in enumerate(skills_map.items()):
    with cols[i % NUM_COLS]:
        with st.container(border=False):
            st.markdown(
                f"""
                <h4 style="text-align:left;font-size: 1.3rem; font-weight: 500; margin-bottom: 0;">
                  <div><span class="highlight-name">{group_name}</span></div>
                </h4>
                """,
                unsafe_allow_html=True,
            )

            selected = st.pills(
                                    "",
                                    group_skills,
                                    selection_mode="multi",
                                    key=f"skills_{i}"
                                )

st.write("")
st.write("")
st.write("")
st.write("")


# -----------------------------
# CERTIFICATIONS
# -----------------------------
st.markdown(
              """            
              <div style="text-align:center; padding: 60px 0 60px 0; scroll-margin-top: 90px;">
              <h2>Certifications</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )


col1, col2, col3 = st.columns(3, vertical_alignment="top")

with col1:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">Math for Data Science & Machine Learning</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Linear Algebra", "Probability & Statistics", "Calculus"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"math_ds_ml"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/ac101ae421c2af93a17d81631182c64f"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )



with col2:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">IBM - Git and GitHub</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Git", "GitHub", "Version Control"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"git_github"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/572e263774b55ba24f15077991a149e8"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )
    
    
with col3:
  with st.container(border=True, height=220, horizontal_alignment="center"):
    st.markdown(
                f"""
                <h4 style="text-align:center;font-size: 1.8rem; font-weight: 500; margin: 0 0 -1px 0;line-height: 1.2;">
                <span class="highlight-name">LLM & LangChain</span>
                </h4>
                """,
                unsafe_allow_html=True,
            )
    selected_categories = ["Prompt Engineering", "AI Agents", "Context Management"]
    categories = st.pills(
                            "",
                            selected_categories,
                            selection_mode="multi",
                            default=selected_categories,
                            key=f"llm_langchain"
                        )
    st.markdown(
                  """
                  <div style="text-align: center;">
                      <a href="https://coursera.org/share/d11de5683f4c12e79340fb4fe51e6afe"
                        target="_blank"
                        class="t-link">
                          ↗︎ View Credentials
                      </a>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )
        

# -----------------------------
# CONTACT
# -----------------------------
st.markdown(
              """            
              <div id="contact" style="text-align:center; padding: 110px 0 0 0; scroll-margin-top: 90px;">
              <h2>Get in Touch</h2>
              </div>
              """,
              unsafe_allow_html=True,
          )

st.markdown(
            """
            <div style="text-align:center; color: #f5c542; font-size:1rem;">
                Let us collaborate and create a better world together!
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
            """         
            <div style="text-align:center; padding-bottom: 20px;">   
                <div style="margin-top: 0px;">
                    <a href="mailto:sundarram1997@arizona.edu" class="cta-button">
                        Send an e-mail
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown(
"""<div class="social-buttons">
  <a class="social-btn"
     href="https://www.linkedin.com/in/sundar-ram-subramanian"
     target="_blank"
     rel="noopener noreferrer"
     aria-label="LinkedIn">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" />
  </a>

  <a class="social-btn"
     href="https://github.com/sundarram1608"
     target="_blank"
     rel="noopener noreferrer"
     aria-label="GitHub">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" />
  </a>
</div>""",
    unsafe_allow_html=True,
)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.divider()

# -----------------------------
# FOOTER
# -----------------------------
# st.caption("Sundar Ram Subramanian ⊙ Built with Streamlit", width = "content", text_alignment = "center")
st.markdown(
            """
            <div style="text-align:center; opacity:0.7; font-size:1rem;">
                ⓒ Jan 2026 ⊙ Sundar Ram Subramanian ⊙ Built with Streamlit
            </div>
            """,
            unsafe_allow_html=True,
        )
