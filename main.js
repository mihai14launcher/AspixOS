document.addEventListener('DOMContentLoaded', () => {
    // GSAP animations
    gsap.from(".hero-content", { duration: 1.5, opacity: 0, y: -50 });

    // Scroll animations
    gsap.registerPlugin(ScrollTrigger);

    // Animate features on scroll
    gsap.utils.toArray(".feature").forEach(feature => {
        gsap.fromTo(feature, { opacity: 0, y: 50 }, {
            opacity: 1,
            y: 0,
            scrollTrigger: {
                trigger: feature,
                start: "top 80%",
                end: "top 30%",
                toggleActions: "play none none reverse",
                scrub: true
            }
        });
    });

    // Animate only the download button
    gsap.fromTo("#download .download-button", 
        {
            opacity: 0,
            scale: 0.8
        }, 
        {
            opacity: 1,
            scale: 1,
            duration: 1,
            scrollTrigger: {
                trigger: "#download",
                start: "top 80%",
                end: "top 30%",
                toggleActions: "play none none reverse",
                scrub: true
            }
        });
});
