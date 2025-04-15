from manim import *
import numpy as np

class HeartConfig:
    HEART_COLOR = "#FF4081"
    GLOW_COLOR = "#FF9E80"
    TEXT_COLOR = "#F44336"
    ACCENT_COLOR = "#FF7043"
    HIGHLIGHT_COLOR = "#FFAB40"
    BACKGROUND_COLOR = "#000000"
    
    LIGHT_AXIS_COLOR = "#42A5F5"
    DARK_AXIS_COLOR = "#FFFFFF"
    
    ANIMATION_SPEED = 1.0
    PULSE_INTENSITY = 1.2
    
    AXES_X_LENGTH = 7
    AXES_Y_LENGTH = 5
    HEART_SCALE = 0.8

class HeartEquationIntegrated(Scene):
    def construct(self):
        self.camera.background_color = HeartConfig.BACKGROUND_COLOR
        
        axes = Axes(
            x_range=(-3, 3, 1),
            y_range=(-2.5, 2.5, 1),
            axis_config={"color": HeartConfig.LIGHT_AXIS_COLOR, "include_tip": False},
            x_length=HeartConfig.AXES_X_LENGTH,
            y_length=HeartConfig.AXES_Y_LENGTH
        )
        axes.shift(UP * 0.5)
        
        x_arrow_pos = Arrow(
            start=axes.c2p(2.8, 0),
            end=axes.c2p(3.2, 0),
            color=HeartConfig.DARK_AXIS_COLOR,
            buff=0,
            max_stroke_width_to_length_ratio=10
        )
        y_arrow_pos = Arrow(
            start=axes.c2p(0, 2.3),
            end=axes.c2p(0, 2.7),
            color=HeartConfig.DARK_AXIS_COLOR,
            buff=0,
            max_stroke_width_to_length_ratio=10
        )
        x_arrow_neg = Arrow(
            start=axes.c2p(-2.8, 0),
            end=axes.c2p(-3.2, 0),
            color=HeartConfig.DARK_AXIS_COLOR,
            buff=0,
            max_stroke_width_to_length_ratio=10
        )
        y_arrow_neg = Arrow(
            start=axes.c2p(0, -2.3),
            end=axes.c2p(0, -2.7),
            color=HeartConfig.DARK_AXIS_COLOR,
            buff=0,
            max_stroke_width_to_length_ratio=10)
        
        self.play(
            Create(axes),
            Create(x_arrow_pos),
            Create(y_arrow_pos),
            Create(x_arrow_neg),
            Create(y_arrow_neg),
            run_time=0.7,
            rate_func=smooth
        )
        
        scale_factor = HeartConfig.HEART_SCALE
        
        def heart_func(x, k_val):
            term1 = np.power(np.abs(x), 2/3)
            term2 = np.zeros_like(x)
            valid_indices = (3 - x**2) > 0
            term2[valid_indices] = 0.9 * np.sin(k_val * x[valid_indices]) * np.sqrt(3 - x[valid_indices]**2)
            return (term1 + term2) * scale_factor
        
        def heart_point(x, k_val):
            term1 = np.power(np.abs(x), 2/3)
            term2 = 0
            if (3 - x**2) > 0:
                term2 = 0.9 * np.sin(k_val * x) * np.sqrt(3 - x**2)
            return (term1 + term2) * scale_factor
        
        k_tracker = ValueTracker(0.0)
        
        traces = VGroup()
        
        def add_trace(k_val):
            trace = axes.plot(
                lambda x: heart_func(x, k_val),
                x_range=[-2, 2, 0.01],
                color=PINK,
                stroke_width=1,
                stroke_opacity=0.2
            )
            traces.add(trace)
            return trace
        
        heart_graph = always_redraw(
            lambda: axes.plot(
                lambda x: heart_func(x, k_tracker.get_value()),
                x_range=[-2, 2, 0.01],
                color=HeartConfig.HEART_COLOR,
                stroke_width=3
            )
        )
        
        heart_glow = always_redraw(
            lambda: axes.plot(
                lambda x: heart_func(x, k_tracker.get_value()),
                x_range=[-2, 2, 0.01],
                color=HeartConfig.GLOW_COLOR,
                stroke_width=6,
                stroke_opacity=0.3
            )
        )
        
        heart_points = []
        for i in range(15):
            x = -2 + i * 4 / 14
            y = heart_point(x, 3.42)
            point = axes.c2p(x, y)
            heart_points.append(point)
        
        particles = VGroup()
        for i in range(15):
            angle = i * TAU / 15
            radius = 1.0
            position = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            color = interpolate_color(PINK, ORANGE, i/15)
            particle = Dot(position, radius=0.03, color=color).set_opacity(0.7)
            particles.add(particle)
        
        stars = VGroup(
            *[Dot(
                point=[np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0],
                radius=np.random.uniform(0.01, 0.03),
                color=RED_E if np.random.random() > 0.5 else PINK
            ).set_opacity(np.random.uniform(0.2, 0.7))
            for _ in range(50)]
        )
        
        self.play(FadeIn(stars, run_time=0.7))
        
        self.play(Create(heart_glow, run_time=0.7))
        
        self.play(Create(heart_graph, run_time=0.8))
        
        self.play(FadeIn(particles, run_time=0.5))
        
        title = Text("Heart Equation", font_size=32)
        title.set_color_by_gradient(PINK, RED, ORANGE)
        title.to_edge(UP)
        self.play(Write(title, run_time=0.8))
        
        equation = MathTex(
            r"y = |x|^{\frac{2}{3}} + 0.9\sin(kx)\sqrt{3-x^2}",
            font_size=32,
        )
        equation.set_color_by_gradient(PINK, RED, ORANGE)
        
        equation.to_edge(DOWN).shift(UP * 0.4)
        self.play(Write(equation, run_time=0.7))
        
        def k_to_color(k):
            colors = [rgb_to_hex(color_to_rgb(PINK)), 
                     rgb_to_hex(color_to_rgb(RED)), 
                     "#FF5722", 
                     "#FF9800", 
                     rgb_to_hex(color_to_rgb(ORANGE))]
            if k <= 0:
                return PINK
            if k >= 100:
                return ORANGE
                
            idx = (k / 100) * (len(colors) - 1)
            idx_low = int(idx)
            idx_high = min(idx_low + 1, len(colors) - 1)
            factor = idx - idx_low
            
            color1 = hex_to_rgb(colors[idx_low])
            color2 = hex_to_rgb(colors[idx_high])
            
            r = color1[0] * (1 - factor) + color2[0] * factor
            g = color1[1] * (1 - factor) + color2[1] * factor
            b = color1[2] * (1 - factor) + color2[2] * factor
            
            return rgb_to_color([r, g, b])
            
        k_value_template = DecimalNumber(
            0.0,
            num_decimal_places=2,
            font_size=28,
        )
        k_value_template.add_updater(lambda m: m.set_value(k_tracker.get_value()))
        k_value_template.add_updater(lambda m: m.set_color(k_to_color(k_tracker.get_value())))
        
        k_label = MathTex("k = ", font_size=28, color=RED)
        k_group = VGroup(k_label, k_value_template).arrange(RIGHT, buff=0.2)
        k_group.next_to(equation, DOWN, buff=0.2)
        
        self.play(Write(k_group, run_time=0.7))
        
        self.wait(0.5)
        
        self.play(
            *[s.animate.shift(np.random.uniform(-0.1, 0.1) * UP + np.random.uniform(-0.1, 0.1) * RIGHT) 
              for s in stars],
            run_time=1.5,
            rate_func=there_and_back
        )
        
        self.play(FadeIn(add_trace(0.0), run_time=0.3))
        
        self.play(
            k_tracker.animate.set_value(3.42),
            *[particles[i].animate.move_to(heart_points[i]) for i in range(len(particles))],
            run_time=2.0,
            rate_func=smooth
        )
        
        self.play(FadeIn(add_trace(3.42), run_time=0.3))
        
        def pulse_heart(heart, glow, intensity=1.2, duration=0.4):
            return AnimationGroup(
                heart.animate.set_stroke(width=5*intensity, color=PINK),
                glow.animate.set_stroke(width=10*intensity, opacity=0.5),
                run_time=duration
            )
        
        self.play(pulse_heart(heart_graph, heart_glow, 1.0, 0.4))
        self.play(
            heart_graph.animate.set_stroke(width=3, color=HeartConfig.HEART_COLOR),
            heart_glow.animate.set_stroke(width=6, opacity=0.3),
            run_time=0.4
        )
        
        k_values_to_trace = [10, 25, 50, 75]
        
        for k_val in k_values_to_trace:
            scatter_points = []
            for i in range(15):
                x = np.random.uniform(-1.5, 1.5)
                y = heart_point(x, k_val)
                scatter_points.append(axes.c2p(x, y))
            
            self.play(
                k_tracker.animate.set_value(k_val),
                *[particles[i].animate.move_to(scatter_points[i]) for i in range(len(particles))],
                run_time=0.8,
                rate_func=smooth
            )
            self.play(FadeIn(add_trace(k_val), run_time=0.2))
        
        self.play(
            k_tracker.animate.set_value(100),
            *[s.animate.shift(np.random.uniform(-0.1, 0.1) * UP + np.random.uniform(-0.1, 0.1) * RIGHT) 
              for s in stars],
            run_time=1.5,
            rate_func=linear
        )
        
        self.play(FadeIn(add_trace(100), run_time=0.3))
        
        self.play(
            k_tracker.animate.set_value(3.42),
            *[particles[i].animate.move_to(heart_points[i]) for i in range(len(particles))],
            run_time=1.5,
            rate_func=there_and_back_with_pause
        )
        
        self.play(pulse_heart(heart_graph, heart_glow, 1.2, 0.5))
        self.play(
            heart_graph.animate.set_stroke(width=3, color=HeartConfig.HEART_COLOR),
            heart_glow.animate.set_stroke(width=6, opacity=0.3),
            run_time=0.5
        )
        
        self.wait(1)