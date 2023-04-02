// Generated from C:/UniversitÓ/Linguaggi/Laboratorio/consegne/VR443470-lab_2/src/ex2\IntExp.g4 by ANTLR 4.12.0
package ex2;
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link IntExpParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface IntExpVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link IntExpParser#main}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMain(IntExpParser.MainContext ctx);
	/**
	 * Visit a parse tree produced by {@link IntExpParser#begin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBegin(IntExpParser.BeginContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nullassignm}
	 * labeled alternative in {@link IntExpParser#dec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNullassignm(IntExpParser.NullassignmContext ctx);
	/**
	 * Visit a parse tree produced by the {@code assignm}
	 * labeled alternative in {@link IntExpParser#dec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignm(IntExpParser.AssignmContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nat}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNat(IntExpParser.NatContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alf}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlf(IntExpParser.AlfContext ctx);
	/**
	 * Visit a parse tree produced by the {@code plus}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPlus(IntExpParser.PlusContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sub}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSub(IntExpParser.SubContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mul}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMul(IntExpParser.MulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code div}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDiv(IntExpParser.DivContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mod}
	 * labeled alternative in {@link IntExpParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMod(IntExpParser.ModContext ctx);
}